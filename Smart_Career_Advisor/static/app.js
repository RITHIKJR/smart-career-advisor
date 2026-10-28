let aptitudeAnswers = {};
let riasecAnswers = {};
let isLoggedIn = false;

// Page Navigation
function showPage(pageName) {
    if (!isLoggedIn && pageName !== 'auth') {
        alert('Please login first');
        return;
    }
    
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
    
    document.getElementById(pageName + 'Page').classList.add('active');
    document.querySelector(`[onclick="showPage('${pageName}')"]`).classList.add('active');
    
    const titles = {
        'auth': 'Welcome',
        'assessment': 'Career Assessments',
        'results': 'Your Results',
        'learning': 'Learning Path',
        'colleges': 'College Recommendations'
    };
    document.getElementById('pageTitle').textContent = titles[pageName];
    
    if (pageName === 'results') loadResults();
    if (pageName === 'learning') loadLearningPath();
}

// Auth Functions
function switchAuth(type) {
    document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');
    
    if (type === 'login') {
        document.getElementById('loginForm').style.display = 'flex';
        document.getElementById('registerForm').style.display = 'none';
    } else {
        document.getElementById('loginForm').style.display = 'none';
        document.getElementById('registerForm').style.display = 'flex';
    }
}

async function register() {
    const username = document.getElementById('regUsername').value;
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;
    const confirm = document.getElementById('regConfirm').value;
    const error = document.getElementById('registerError');
    
    if (password !== confirm) {
        error.textContent = 'Passwords do not match';
        return;
    }
    if (password.length < 6) {
        error.textContent = 'Password must be at least 6 characters';
        return;
    }
    
    const res = await fetch('/api/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, email, password})
    });
    
    const data = await res.json();
    if (data.success) {
        error.style.color = 'green';
        error.textContent = 'Registration successful! Please login.';
        setTimeout(() => switchAuth('login'), 1500);
    } else {
        error.textContent = data.message;
    }
}

async function login() {
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    const error = document.getElementById('loginError');
    
    const res = await fetch('/api/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password})
    });
    
    const data = await res.json();
    if (data.success) {
        isLoggedIn = true;
        document.getElementById('userInfo').style.display = 'flex';
        document.getElementById('userName').textContent = username;
        document.getElementById('logoutBtn').style.display = 'block';
        
        loadAptitudeQuestions();
        loadRiasecQuestions();
        showPage('assessment');
    } else {
        error.textContent = data.message;
    }
}

async function logout() {
    await fetch('/api/logout', {method: 'POST'});
    location.reload();
}

// Test Functions
function switchTest(type) {
    document.querySelectorAll('.test-tab').forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');
    
    if (type === 'aptitude') {
        document.getElementById('aptitudeTest').style.display = 'block';
        document.getElementById('riasecTest').style.display = 'none';
    } else {
        document.getElementById('aptitudeTest').style.display = 'none';
        document.getElementById('riasecTest').style.display = 'block';
    }
}

async function loadAptitudeQuestions() {
    const res = await fetch('/api/aptitude-questions');
    const data = await res.json();
    const container = document.getElementById('aptitudeQuestions');
    
    container.innerHTML = '';
    data.questions.forEach((q, i) => {
        container.innerHTML += `
            <div class="question">
                <h4>Q${i+1}. ${q.q}</h4>
                <div class="options">
                    ${q.options.map((opt, j) => `
                        <label class="option">
                            <input type="radio" name="q${i}" value="${j}" onchange="aptitudeAnswers[${i}]=${j}">
                            ${opt}
                        </label>
                    `).join('')}
                </div>
            </div>
        `;
    });
}

async function loadRiasecQuestions() {
    const res = await fetch('/api/riasec-questions');
    const data = await res.json();
    const container = document.getElementById('riasecQuestions');
    
    container.innerHTML = '';
    data.questions.forEach((q, i) => {
        container.innerHTML += `
            <div class="question">
                <h4>${q.q}</h4>
                <div class="riasec-scale">
                    ${[1,2,3,4,5].map(val => `
                        <label>
                            <input type="radio" name="r${i}" value="${val}" onchange="riasecAnswers[${i}]={type:'${q.type}',value:${val}}">
                            <span>${val}</span>
                        </label>
                    `).join('')}
                </div>
            </div>
        `;
    });
}

async function submitAptitude() {
    const res = await fetch('/api/aptitude-questions');
    const data = await res.json();
    
    let score = 0;
    data.questions.forEach((q, i) => {
        if (aptitudeAnswers[i] === q.answer) score++;
    });
    
    alert(`Aptitude Score: ${score}/10\nNow complete the RIASEC test!`);
    switchTest('riasec');
}

async function submitRiasec() {
    const res = await fetch('/api/aptitude-questions');
    const aptData = await res.json();
    
    let aptScore = 0;
    aptData.questions.forEach((q, i) => {
        if (aptitudeAnswers[i] === q.answer) aptScore++;
    });
    
    const riasecScores = {R:0, I:0, A:0, S:0, E:0, C:0};
    Object.values(riasecAnswers).forEach(ans => {
        riasecScores[ans.type] += ans.value;
    });
    
    const result = await fetch('/api/submit-assessment', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            aptitude_score: aptScore,
            riasec_scores: riasecScores
        })
    });
    
    const resultData = await result.json();
    if (resultData.success) {
        alert('Assessment completed! Check Results page.');
        showPage('results');
    }
}

async function loadResults() {
    const res = await fetch('/api/get-assessment');
    const data = await res.json();
    const container = document.getElementById('resultsContent');
    
    if (data.success) {
        container.innerHTML = `
            <div class="result-box">
                <h3>🎯 Your Career Profile</h3>
                <p><strong>Aptitude Score:</strong> ${data.aptitude_score}/10</p>
                <p><strong>RIASEC Type:</strong> ${data.riasec_type}</p>
                <p><strong>Recommended Branch:</strong> ${data.recommended_branch}</p>
                <p><strong>Date:</strong> ${data.completed_date}</p>
            </div>
            <button onclick="showPage('learning')" class="btn-submit">View Learning Path →</button>
        `;
    } else {
        container.innerHTML = '<p>Complete the assessment first!</p>';
    }
}

async function loadLearningPath() {
    const assessRes = await fetch('/api/get-assessment');
    const assessData = await assessRes.json();
    
    if (!assessData.success) {
        document.getElementById('learningContent').innerHTML = '<p>Complete assessment first!</p>';
        return;
    }
    
    const branch = assessData.recommended_branch;
    const pathRes = await fetch(`/api/learning-path/${branch}`);
    const pathData = await pathRes.json();
    
    const progressRes = await fetch('/api/get-progress');
    const progressData = await progressRes.json();
    const completed = progressData.success ? progressData.progress : {};
    
    const container = document.getElementById('learningContent');
    container.innerHTML = `<h3>Learning Path for ${branch}</h3>`;
    
    pathData.modules.forEach((mod, i) => {
        const isComplete = completed[i] || false;
        const progress = isComplete ? 100 : 0;
        
        container.innerHTML += `
            <div class="module-card">
                <h4>Module ${i+1}: ${mod.module}</h4>
                <p><strong>Duration:</strong> ${mod.duration}</p>
                <div class="topics">
                    ${mod.topics.map(t => `<span class="topic-tag">${t}</span>`).join('')}
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width:${progress}%">${progress}%</div>
                </div>
                ${!isComplete ? `<button class="btn-submit complete-btn" onclick="markComplete(${i}, '${branch}')">Mark Complete</button>` : '<p style="color:green;">✓ Completed</p>'}
            </div>
        `;
    });
}

async function markComplete(moduleIndex, branch) {
    const progressRes = await fetch('/api/get-progress');
    const progressData = await progressRes.json();
    const progress = progressData.success ? progressData.progress : {};
    
    progress[moduleIndex] = true;
    
    const pathRes = await fetch(`/api/learning-path/${branch}`);
    const pathData = await pathRes.json();
    
    await fetch('/api/save-progress', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            branch: branch,
            modules: pathData.modules,
            progress: progress
        })
    });
    
    loadLearningPath();
}

async function getRecommendations() {
    const cutoff = document.getElementById('cutoff').value;
    const category = document.getElementById('category').value;
    const branch = document.getElementById('branch').value;
    
    if (!cutoff) {
        alert('Please enter your cutoff');
        return;
    }
    
    const res = await fetch('/api/recommend', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({cutoff, category, branch})
    });
    
    const data = await res.json();
    const results = document.getElementById('collegeResults');
    
    if (data.success && data.data.length > 0) {
        results.innerHTML = '<h3>Top Recommended Colleges</h3>';
        data.data.forEach(rec => {
            results.innerHTML += `
                <div class="result-card">
                    <h3>${rec.code} - ${rec.name}</h3>
                    <p><strong>Branch:</strong> ${rec.branch}</p>
                    <p><strong>Required Cutoff:</strong> ${rec.cutoff}</p>
                    <p class="probability">Admission Probability: ${rec.probability}%</p>
                </div>
            `;
        });
    } else {
        results.innerHTML = '<p>No colleges found for your criteria</p>';
    }
}
