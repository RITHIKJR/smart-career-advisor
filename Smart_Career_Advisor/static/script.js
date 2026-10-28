let aptitudeAnswers = {};
let riasecAnswers = {};

function switchToLogin() {
    document.getElementById('loginForm').style.display = 'flex';
    document.getElementById('registerForm').style.display = 'none';
    document.getElementById('authTitle').textContent = 'Welcome Back';
    document.getElementById('authSubtitle').textContent = 'Sign in to continue your journey';
}

function switchToRegister() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'flex';
    document.getElementById('authTitle').textContent = 'Create Account';
    document.getElementById('authSubtitle').textContent = 'Join us to start your career journey';
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
        error.textContent = 'Registration successful! Redirecting...';
        setTimeout(() => switchToLogin(), 1500);
    } else {
        error.style.color = 'red';
        error.textContent = data.message;
    }
}

async function login() {
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    const error = document.getElementById('loginError');
    
    const res = await fetch('/api/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email, password})
    });
    
    const data = await res.json();
    if (data.success) {
        document.getElementById('authSection').style.display = 'none';
        document.getElementById('mainSection').style.display = 'block';
        document.getElementById('username').textContent = data.username;
        checkAssessmentStatus();
    } else {
        error.textContent = data.message;
    }
}

async function logout() {
    await fetch('/api/logout', {method: 'POST'});
    location.reload();
}

function showSection(section) {
    document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.section').forEach(s => s.style.display = 'none');
    
    event.target.classList.add('active');
    document.getElementById(section + 'Section').style.display = 'block';
    
    if (section === 'dashboard') loadDashboard();
    if (section === 'results') loadResults();
    if (section === 'learning') loadLearningPath();
    if (section === 'colleges') loadCollegeSection();
    if (section === 'scholarships') loadScholarships();
    if (section === 'goals') loadGoals();
    if (section === 'notes') loadNotes();
}

async function checkAssessmentStatus() {
    const res = await fetch('/api/get-assessment');
    const data = await res.json();
    if (data.success) {
        document.querySelector('.nav-tab:nth-child(3)').innerHTML = '📊 Results ✓';
    }
    loadDashboard();
}

async function loadResults() {
    const res = await fetch('/api/get-assessment');
    const data = await res.json();
    const container = document.getElementById('resultsContent');
    const placementSection = document.getElementById('placementStatsSection');
    
    if (data.success) {
        container.innerHTML = `
            <div class="result-box">
                <h3>🎯 Your Career Profile</h3>
                <p><strong>Aptitude Score:</strong> ${data.aptitude_score}/10</p>
                <p><strong>RIASEC Type:</strong> ${data.riasec_type}</p>
                <p><strong>Recommended Course:</strong> ${data.recommended_branch}</p>
                <p><strong>Assessment Date:</strong> ${data.completed_date}</p>
            </div>
            <div style="margin-top: 20px;">
                <label style="font-weight: 600; color: #374151; margin-bottom: 8px; display: block;">View Learning Path For:</label>
                <select id="resultsBranchSelect" onchange="loadResultsForBranch()" style="width: 100%; padding: 12px; border: 2px solid #e5e7eb; border-radius: 10px; font-size: 15px; margin-bottom: 15px;">
                    <option value="${data.recommended_branch}">${data.recommended_branch} (Recommended)</option>
                    <option value="Computer Science and Engineering">Computer Science and Engineering</option>
                    <option value="Information Technology">Information Technology</option>
                    <option value="Electronics and Communication Engineering">Electronics and Communication Engineering</option>
                    <option value="Electrical and Electronics Engineering">Electrical and Electronics Engineering</option>
                    <option value="Mechanical Engineering">Mechanical Engineering</option>
                    <option value="Civil Engineering">Civil Engineering</option>
                    <option value="Bio Medical Engineering">Bio Medical Engineering</option>
                    <option value="Industrial Engineering">Industrial Engineering</option>
                    <option value="Computer Science and Design">Computer Science and Design</option>
                </select>
            </div>
            <button onclick="showSection('learning')" class="btn-auth" style="width: auto; padding: 14px 32px;">View Learning Path →</button>
        `;
        
        // Remove duplicate option
        const select = document.getElementById('resultsBranchSelect');
        const options = Array.from(select.options);
        const seen = new Set();
        options.forEach(opt => {
            if (seen.has(opt.value)) {
                opt.remove();
            } else {
                seen.add(opt.value);
            }
        });
        
        loadResultsForBranch();
    } else {
        container.innerHTML = '<p>Complete the assessment first!</p>';
        placementSection.style.display = 'none';
    }
}

async function loadResultsForBranch() {
    const select = document.getElementById('resultsBranchSelect');
    const branch = select ? select.value : null;
    if (!branch) return;
    
    const placementSection = document.getElementById('placementStatsSection');
    const placementRes = await fetch(`/api/placement-stats/${branch}`);
    const placementData = await placementRes.json();
    
    if (placementData.success) {
        const p = placementData.placement;
        const insights = placementData.insights;
        placementSection.style.display = 'block';
        placementSection.innerHTML = `
            <h3>${p.icon} Placement Statistics for ${branch}</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 20px;">
                <div class="stat-card">
                    <div class="stat-icon">💰</div>
                    <div class="stat-value">${p.avg_package}</div>
                    <div class="stat-label">Average Package</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">🏆</div>
                    <div class="stat-value">${p.top_package}</div>
                    <div class="stat-label">Top Package</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">📊</div>
                    <div class="stat-value">${p.placement_rate}</div>
                    <div class="stat-label">Placement Rate</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">📈</div>
                    <div class="stat-value">${p.growth_trend}</div>
                    <div class="stat-label">Market Trend</div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px;">
                <div class="info-card">
                    <h4>🏢 Top Recruiters</h4>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                        ${p.top_recruiters.map(r => `<span class="topic-tag" style="background: #dbeafe; color: #1e40af;">${r}</span>`).join('')}
                    </div>
                </div>
                <div class="info-card">
                    <h4>💼 Job Roles</h4>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                        ${p.job_roles.map(r => `<span class="topic-tag" style="background: #dcfce7; color: #166534;">${r}</span>`).join('')}
                    </div>
                </div>
            </div>
            
            <div class="info-card" style="margin-top: 20px;">
                <h4>🎓 Career Insights</h4>
                <div style="margin-top: 15px;">
                    <p style="margin-bottom: 10px;"><strong>💡 Skills Required:</strong></p>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 15px;">
                        ${insights.skills_required.map(s => `<span class="topic-tag" style="background: #fef3c7; color: #92400e;">${s}</span>`).join('')}
                    </div>
                    <p style="margin-bottom: 8px;"><strong>📚 Higher Studies Options:</strong> ${insights.higher_studies.join(', ')}</p>
                    <p style="margin-bottom: 8px;"><strong>🚀 Startup Potential:</strong> ${insights.startup_potential}</p>
                    <p><strong>🏠 Remote Work:</strong> ${insights.remote_work}</p>
                </div>
            </div>
        `;
    }
}

async function loadLearningPath() {
    const assessRes = await fetch('/api/get-assessment');
    const assessData = await assessRes.json();
    
    if (!assessData.success) {
        document.getElementById('learningContent').innerHTML = '<p>Complete assessment first!</p>';
        return;
    }
    
    const container = document.getElementById('learningContent');
    container.innerHTML = `
        <div style="margin-bottom: 20px;">
            <label style="font-weight: 600; color: #374151; margin-bottom: 8px; display: block;">Select Course:</label>
            <select id="learningBranchSelect" onchange="loadLearningForBranch()" style="width: 100%; padding: 12px; border: 2px solid #e5e7eb; border-radius: 10px; font-size: 15px;">
                <option value="${assessData.recommended_branch}">${assessData.recommended_branch} (Recommended)</option>
                <option value="Computer Science and Engineering">Computer Science and Engineering</option>
                <option value="Information Technology">Information Technology</option>
                <option value="Electronics and Communication Engineering">Electronics and Communication Engineering</option>
                <option value="Electrical and Electronics Engineering">Electrical and Electronics Engineering</option>
                <option value="Mechanical Engineering">Mechanical Engineering</option>
                <option value="Civil Engineering">Civil Engineering</option>
                <option value="Bio Medical Engineering">Bio Medical Engineering</option>
                <option value="Industrial Engineering">Industrial Engineering</option>
                <option value="Computer Science and Design">Computer Science and Design</option>
            </select>
        </div>
        <div id="learningModules"></div>
    `;
    
    // Remove duplicate option
    const select = document.getElementById('learningBranchSelect');
    const options = Array.from(select.options);
    const seen = new Set();
    options.forEach(opt => {
        if (seen.has(opt.value)) {
            opt.remove();
        } else {
            seen.add(opt.value);
        }
    });
    
    loadLearningForBranch();
}

async function loadLearningForBranch() {
    const select = document.getElementById('learningBranchSelect');
    const branch = select ? select.value : null;
    if (!branch) return;
    
    const pathRes = await fetch(`/api/learning-path/${branch}`);
    const pathData = await pathRes.json();
    
    const progressRes = await fetch('/api/get-progress');
    const progressData = await progressRes.json();
    const completed = progressData.success ? progressData.progress : {};
    
    const coursesRes = await fetch('/api/external-courses');
    const coursesData = await coursesRes.json();
    const userCourses = coursesData.success ? coursesData.courses : [];
    
    const modulesContainer = document.getElementById('learningModules');
    modulesContainer.innerHTML = `<h3>Learning Path for ${branch}</h3>`;
    
    pathData.modules.forEach((mod, i) => {
        const isComplete = completed[i] || false;
        const progress = isComplete ? 100 : 0;
        const moduleCourses = userCourses.filter(c => c.module === mod.module);
        const completedCourses = moduleCourses.filter(c => c.completed === 1).length;
        
        let coursesHTML = '';
        if (mod.courses && mod.courses.length > 0) {
            coursesHTML = `
                <div style="margin-top: 15px; padding: 15px; background: #f9fafb; border-radius: 8px;">
                    <h5 style="margin: 0 0 10px 0; color: #374151;">📚 Recommended Courses (${completedCourses}/${mod.courses.length} completed)</h5>
                    ${mod.courses.map(course => {
                        const started = moduleCourses.find(c => c.url === course.url);
                        const isCompleted = started && started.completed === 1;
                        return `
                            <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: white; border-radius: 6px; margin-bottom: 8px; border-left: 3px solid ${isCompleted ? '#10b981' : started ? '#f59e0b' : '#6366f1'};">
                                <div style="flex: 1;">
                                    <div style="font-weight: 600; color: #111827;">${course.name} ${isCompleted ? '✅' : ''}</div>
                                    <div style="font-size: 13px; color: #6b7280;">
                                        <span style="background: ${course.platform === 'Coursera' ? '#0056D2' : course.platform === 'YouTube' ? '#FF0000' : '#A435F0'}; color: white; padding: 2px 8px; border-radius: 4px; margin-right: 8px;">${course.platform}</span>
                                        ${course.free ? '<span style="color: #10b981;">🆓 Free</span>' : '<span style="color: #f59e0b;">💰 Paid</span>'}
                                    </div>
                                </div>
                                <div style="display: flex; gap: 8px;">
                                    ${!started ? `
                                        <button onclick="startCourse('${mod.module}', '${course.platform}', '${course.name}', '${course.url}')" style="padding: 6px 12px; background: #6366f1; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 13px;">🚀 Start Course</button>
                                    ` : !isCompleted ? `
                                        <a href="${course.url}" target="_blank" style="padding: 6px 12px; background: #374151; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; text-decoration: none; display: inline-block;">🔗 Visit Course</a>
                                        <button onclick="completeCourse(${started.id})" style="padding: 6px 12px; background: #10b981; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 13px;">✓ Mark Complete</button>
                                    ` : `
                                        <a href="${course.url}" target="_blank" style="padding: 6px 12px; background: #374151; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; text-decoration: none; display: inline-block;">🔗 Revisit</a>
                                    `}
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
            `;
        }
        
        modulesContainer.innerHTML += `
            <div class="module-card">
                <h4>Module ${i+1}: ${mod.module}</h4>
                <p><strong>Duration:</strong> ${mod.duration}</p>
                <div class="topics">
                    ${mod.topics.map(t => `<span class="topic-tag">${t}</span>`).join('')}
                </div>
                ${coursesHTML}
                <div class="progress-bar">
                    <div class="progress-fill" style="width:${progress}%">${progress}%</div>
                </div>
                <button onclick="markComplete(${i}, '${branch}')" style="width: 100%; padding: 14px; background: ${isComplete ? '#6b7280' : '#10b981'}; color: white; border: none; border-radius: 10px; font-size: 16px; font-weight: 600; cursor: pointer; margin-top: 15px;">${isComplete ? '❌ Unmark Module' : '✓ Mark Module as Complete'}</button>
            </div>
        `;
    });
}

async function markComplete(moduleIndex, branch) {
    const progressRes = await fetch('/api/get-progress');
    const progressData = await progressRes.json();
    const progress = progressData.success ? progressData.progress : {};
    
    // Toggle completion status
    progress[moduleIndex] = !progress[moduleIndex];
    
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
    
    if (progress[moduleIndex]) {
        await fetch('/api/study-streak', {method: 'POST'});
    }
    loadLearningPath();
    loadDashboard();
}

async function loadCollegeSection() {
    const assessRes = await fetch('/api/get-assessment');
    const assessData = await assessRes.json();
    
    if (assessData.success) {
        // Pre-select the recommended course from assessment
        document.getElementById('courseBranch').value = assessData.recommended_branch;
    }
}

async function getRecommendations() {
    const cutoff = document.getElementById('cutoff').value;
    const category = document.getElementById('category').value;
    const branch = document.getElementById('courseBranch').value;
    
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
        data.data.forEach((rec, index) => {
            const typeInfo = rec.college_type;
            const locationInfo = rec.location;
            const locationDisplay = locationInfo 
                ? `<p style="color: #6b7280; font-size: 14px;">📍 ${locationInfo.city}, ${locationInfo.area}</p>`
                : '';
            const mapButton = rec.maps_url 
                ? `<a href="${rec.maps_url}" target="_blank" class="btn-auth" style="display: inline-block; width: auto; padding: 8px 16px; margin-top: 10px; font-size: 14px; text-decoration: none;">📍 View on Map</a>`
                : '';
            
            results.innerHTML += `
                <div class="result-card">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 12px;">
                        <h3 style="margin: 0; flex: 1;">${rec.code} - ${rec.name}</h3>
                        <span style="background: ${typeInfo.color}; color: white; padding: 6px 12px; border-radius: 20px; font-size: 13px; font-weight: 600; white-space: nowrap;">
                            ${typeInfo.badge}
                        </span>
                    </div>
                    ${locationDisplay}
                    <p><strong>Branch:</strong> ${rec.branch}</p>
                    <p><strong>Required Cutoff:</strong> ${rec.cutoff}</p>
                    <p class="probability">Admission Probability: ${rec.probability}%</p>
                    <p style="color: #6b7280; font-size: 14px; margin-top: 8px;">💡 ${typeInfo.description}</p>
                    ${mapButton}
                </div>
            `;
        });
    } else {
        results.innerHTML = '<p class="error">No colleges found for your criteria ❌</p>';
    }
}

async function loadDashboard() {
    const statsRes = await fetch('/api/dashboard-stats');
    const stats = await statsRes.json();
    
    if (stats.success) {
        document.getElementById('streakValue').textContent = stats.current_streak;
        document.getElementById('modulesValue').textContent = `${stats.completed_modules}/${stats.total_modules}`;
        document.getElementById('goalsValue').textContent = `${stats.completed_goals}/${stats.total_goals}`;
    }
    
    const streakRes = await fetch('/api/get-streak');
    const streak = await streakRes.json();
    if (streak.success) {
        document.getElementById('totalDaysValue').textContent = streak.total_days;
    }
    
    const achievements = document.getElementById('achievementsContent');
    achievements.innerHTML = '';
    
    if (stats.assessment_completed) {
        achievements.innerHTML += '<div class="achievement-badge">✅ Assessment Complete</div>';
    }
    if (stats.current_streak >= 7) {
        achievements.innerHTML += '<div class="achievement-badge">🔥 Week Warrior</div>';
    }
    if (stats.completed_modules >= 3) {
        achievements.innerHTML += '<div class="achievement-badge">🏆 Learning Champion</div>';
    }
    if (stats.completed_goals >= 5) {
        achievements.innerHTML += '<div class="achievement-badge">🎯 Goal Crusher</div>';
    }
    if (achievements.innerHTML === '') {
        achievements.innerHTML = '<p style="color: #6b7280;">Complete tasks to unlock achievements!</p>';
    }
}

async function loadGoals() {
    const res = await fetch('/api/goals');
    const data = await res.json();
    const container = document.getElementById('goalsContent');
    
    if (data.success && data.goals.length > 0) {
        container.innerHTML = '';
        data.goals.forEach(goal => {
            container.innerHTML += `
                <div class="goal-item ${goal.completed ? 'completed' : ''}">
                    <div class="goal-text">${goal.text}</div>
                    <div class="goal-date">📅 ${goal.target}</div>
                    <input type="checkbox" class="goal-check" ${goal.completed ? 'checked' : ''} onchange="toggleGoal(${goal.id})">
                </div>
            `;
        });
    } else {
        container.innerHTML = '<p style="color: #6b7280;">No goals yet. Set your first goal above!</p>';
    }
}

async function addGoal() {
    const text = document.getElementById('goalText').value;
    const date = document.getElementById('goalDate').value;
    
    if (!text || !date) {
        alert('Please fill in all fields');
        return;
    }
    
    await fetch('/api/goals', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({goal_text: text, target_date: date})
    });
    
    document.getElementById('goalText').value = '';
    document.getElementById('goalDate').value = '';
    loadGoals();
}

async function toggleGoal(goalId) {
    await fetch(`/api/goals/${goalId}/toggle`, {method: 'POST'});
    await fetch('/api/study-streak', {method: 'POST'});
    loadGoals();
    loadDashboard();
}

async function loadNotes() {
    const res = await fetch('/api/notes');
    const data = await res.json();
    const container = document.getElementById('notesContent');
    
    if (data.success && data.notes.length > 0) {
        container.innerHTML = '';
        data.notes.forEach(note => {
            container.innerHTML += `
                <div class="note-item">
                    <div class="note-header">
                        <div class="note-module">📚 ${note.module}</div>
                        <div class="note-date">${note.date}</div>
                    </div>
                    <div class="note-text">${note.text}</div>
                </div>
            `;
        });
    } else {
        container.innerHTML = '<p style="color: #6b7280;">No notes yet. Start taking notes above!</p>';
    }
}

async function addNote() {
    const module = document.getElementById('noteModule').value;
    const text = document.getElementById('noteText').value;
    
    if (!module || !text) {
        alert('Please fill in all fields');
        return;
    }
    
    await fetch('/api/notes', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({module_name: module, note_text: text})
    });
    
    document.getElementById('noteModule').value = '';
    document.getElementById('noteText').value = '';
    loadNotes();
}

let currentScholarships = [];

async function loadScholarships() {
    await filterScholarships();
    loadSuccessStories();
}

async function filterScholarships() {
    const category = document.getElementById('scholarshipCategory').value;
    const type = document.getElementById('scholarshipType').value;
    const firstGrad = document.getElementById('firstGraduate').value;
    
    const res = await fetch(`/api/scholarships?category=${category}&type=${type}&first_graduate=${firstGrad}`);
    const data = await res.json();
    
    if (data.success) {
        currentScholarships = data.scholarships;
        displayScholarships(data.scholarships);
    }
}

function displayScholarships(scholarships) {
    const container = document.getElementById('scholarshipsContent');
    
    if (scholarships.length === 0) {
        container.innerHTML = '<p style="color: #6b7280; text-align: center; padding: 40px;">No scholarships found matching your criteria.</p>';
        return;
    }
    
    container.innerHTML = '';
    scholarships.forEach(s => {
        const tagClass = s.type === 'Government' ? 'tag-government' : s.type === 'State' ? 'tag-state' : 'tag-private';
        container.innerHTML += `
            <div class="scholarship-card">
                <div class="scholarship-header">
                    <div>
                        <div class="scholarship-title">${s.name}</div>
                        <div class="scholarship-provider">🏛️ ${s.provider}</div>
                    </div>
                    <div class="scholarship-amount">💰 ${s.amount}</div>
                </div>
                
                <div class="scholarship-tags">
                    <span class="tag ${tagClass}">${s.type}</span>
                    ${s.first_graduate ? '<span class="tag tag-first-grad">⭐ First Graduate</span>' : ''}
                    <span class="tag" style="background: #f3f4f6; color: #374151;">📅 Deadline: ${s.deadline}</span>
                </div>
                
                <div class="scholarship-details">
                    <p><strong>Description:</strong> ${s.description}</p>
                    <div style="margin-top: 12px;">
                        <strong>Eligibility:</strong>
                        <div class="eligibility-item">Category: ${s.eligibility.category.join(', ')}</div>
                        <div class="eligibility-item">Income: ${s.eligibility.income}</div>
                        <div class="eligibility-item">Merit: ${s.eligibility.merit}</div>
                        <div class="eligibility-item">Branch: ${s.eligibility.branch}</div>
                    </div>
                    <div style="margin-top: 12px;">
                        <strong>Required Documents:</strong>
                        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px;">
                            ${s.documents.map(doc => `<span class="topic-tag" style="background: #e0e7ff; color: #4338ca;">📝 ${doc}</span>`).join('')}
                        </div>
                    </div>
                </div>
                
                <div class="scholarship-actions">
                    <button class="btn-save" onclick="saveScholarship(${s.id})">❤️ Save</button>
                    <button class="btn-apply" onclick="window.open('${s.apply_link}', '_blank')">🚀 Apply Now</button>
                    <button class="btn-details" onclick="showScholarshipDetails(${s.id})">View Details</button>
                </div>
            </div>
        `;
    });
}

async function saveScholarship(scholarshipId) {
    await fetch('/api/scholarships/save', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({scholarship_id: scholarshipId})
    });
    alert('❤️ Scholarship saved! Check "Saved" tab.');
}

function showScholarshipTab(tab) {
    document.querySelectorAll('#scholarshipsSection .nav-tab').forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');
    
    document.getElementById('allScholarshipsTab').style.display = tab === 'all' ? 'block' : 'none';
    document.getElementById('savedScholarshipsTab').style.display = tab === 'saved' ? 'block' : 'none';
    document.getElementById('storiesTab').style.display = tab === 'stories' ? 'block' : 'none';
    
    if (tab === 'saved') loadSavedScholarships();
}

async function loadSavedScholarships() {
    const res = await fetch('/api/scholarships/saved');
    const data = await res.json();
    const container = document.getElementById('savedScholarshipsContent');
    
    if (data.success && data.scholarships.length > 0) {
        container.innerHTML = '';
        data.scholarships.forEach(s => {
            const applied = data.applied_ids.includes(s.id);
            container.innerHTML += `
                <div class="scholarship-card" style="border-left-color: ${applied ? '#10b981' : '#f59e0b'};">
                    <div class="scholarship-header">
                        <div>
                            <div class="scholarship-title">${s.name} ${applied ? '✅' : ''}</div>
                            <div class="scholarship-provider">${s.provider}</div>
                        </div>
                        <div class="scholarship-amount">${s.amount}</div>
                    </div>
                    <p style="margin: 12px 0; color: #374151;">${s.description}</p>
                    <p style="color: #6b7280; font-size: 14px;">📅 Deadline: ${s.deadline}</p>
                    <div class="scholarship-actions">
                        <button class="btn-apply" onclick="toggleApplied(${s.id})">
                            ${applied ? '✅ Applied' : '📝 Mark as Applied'}
                        </button>
                        <button class="btn-apply" onclick="window.open('${s.apply_link}', '_blank')">🚀 Apply Now</button>
                    </div>
                </div>
            `;
        });
    } else {
        container.innerHTML = '<p style="color: #6b7280; text-align: center; padding: 40px;">No saved scholarships yet. Browse and save scholarships from "All Scholarships" tab.</p>';
    }
}

async function toggleApplied(scholarshipId) {
    await fetch('/api/scholarships/toggle-applied', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({scholarship_id: scholarshipId})
    });
    loadSavedScholarships();
}

async function loadSuccessStories() {
    const res = await fetch('/api/scholarships/success-stories');
    const data = await res.json();
    const container = document.getElementById('storiesContent');
    
    if (data.success) {
        container.innerHTML = '<h3 style="color: #92400e; margin-bottom: 20px;">🌟 Inspiring Success Stories</h3>';
        data.stories.forEach(story => {
            container.innerHTML += `
                <div class="story-card">
                    <div class="story-header">
                        <div class="story-name">🎓 ${story.name}</div>
                        <div class="story-year">${story.year}</div>
                    </div>
                    <div class="story-scholarship">🏆 ${story.scholarship} | ${story.branch}</div>
                    <div class="story-text">"${story.story}"</div>
                </div>
            `;
        });
    }
}

function showScholarshipDetails(scholarshipId) {
    const scholarship = currentScholarships.find(s => s.id === scholarshipId);
    if (scholarship) {
        alert(`💰 ${scholarship.name}\n\n🏛️ Provider: ${scholarship.provider}\n💵 Amount: ${scholarship.amount}\n📅 Deadline: ${scholarship.deadline}\n\n📝 Description:\n${scholarship.description}\n\n✅ Eligibility:\n- Category: ${scholarship.eligibility.category.join(', ')}\n- Income: ${scholarship.eligibility.income}\n- Merit: ${scholarship.eligibility.merit}\n- Branch: ${scholarship.eligibility.branch}\n\n📄 Documents Required:\n${scholarship.documents.map((d, i) => `${i+1}. ${d}`).join('\n')}`);
    }
}

async function startCourse(moduleName, platform, courseName, url) {
    await fetch('/api/external-courses/start', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({module_name: moduleName, platform: platform, course_name: courseName, url: url})
    });
    await fetch('/api/study-streak', {method: 'POST'});
    window.open(url, '_blank');
    loadLearningPath();
    loadDashboard();
}

async function completeCourse(courseId) {
    await fetch('/api/external-courses/complete', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({course_id: courseId})
    });
    await fetch('/api/study-streak', {method: 'POST'});
    loadLearningPath();
    loadDashboard();
}


