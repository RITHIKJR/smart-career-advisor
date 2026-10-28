let aptitudeAnswers = {};
let riasecAnswers = {};

// Load aptitude questions on page load
window.onload = function() {
    checkSession();
    if (window.location.pathname.includes('aptitude')) {
        loadAptitudeQuestions();
    } else if (window.location.pathname.includes('riasec')) {
        loadRiasecQuestions();
    }
};

async function checkSession() {
    const res = await fetch('/api/check-session');
    const data = await res.json();
    if (!data.logged_in) {
        alert('Session expired. Please login again.');
        window.location.href = '/dashboard';
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
                <h4>${i+1}. ${q.q}</h4>
                <div class="riasec-scale">
                    ${[1,2,3,4,5].map(val => `
                        <label style="cursor: pointer;">
                            <input type="radio" name="r${i}" value="${val}" onchange="riasecAnswers[${i}]={type:'${q.type}',value:${val}}">
                            <span style="display: block; margin-top: 5px;">${val}</span>
                        </label>
                    `).join('')}
                </div>
                <div style="display:flex;justify-content:space-between;font-size:12px;color:#6b7280;margin-top:8px;">
                    <span>Strongly Disagree</span>
                    <span>Strongly Agree</span>
                </div>
            </div>
        `;
    });
}

async function submitAptitude() {
    const res = await fetch('/api/aptitude-questions');
    const data = await res.json();
    
    // Check if all questions are answered
    if (Object.keys(aptitudeAnswers).length !== data.questions.length) {
        alert('Please answer all questions before submitting!');
        return;
    }
    
    let score = 0;
    data.questions.forEach((q, i) => {
        if (aptitudeAnswers[i] === q.answer) score++;
    });
    
    // Store score in session storage
    sessionStorage.setItem('aptitude_score', score);
    
    alert(`Aptitude Score: ${score}/10\n\nGreat! Now let's discover your personality type with the RIASEC test.`);
    window.location.href = '/riasec';
}

async function submitRiasec() {
    const res = await fetch('/api/riasec-questions');
    const data = await res.json();
    
    // Check if all questions are answered
    if (Object.keys(riasecAnswers).length !== data.questions.length) {
        alert('Please answer all questions before submitting!');
        return;
    }
    
    const aptScore = parseInt(sessionStorage.getItem('aptitude_score') || '0');
    
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
        sessionStorage.removeItem('aptitude_score');
        alert(`Assessment Completed!\n\nYour RIASEC Type: ${resultData.riasec_type}\nRecommended Course: ${resultData.recommended_branch}\n\nYou will now be redirected to the dashboard.`);
        window.location.href = '/dashboard';
    } else {
        alert('Error submitting assessment. Please try again.');
    }
}
