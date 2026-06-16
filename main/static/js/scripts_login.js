loginForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                password: password
            }),
            credentials: 'include'
        });

        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
            throw new Error('پاسخ سرور معتبر نیست');
        }

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'خطا در احراز هویت');
        }

        if (!data.token) {
            throw new Error('توکن احراز هویت دریافت نشد');
        }


        localStorage.setItem('token', data.token);
        if (data.username) {
            localStorage.setItem('username', data.username);
        }


        alert(`خوش آمدید ${data.username || 'کاربر'}!`);
        window.location.href = '/cities/';


    } catch (error) {
        console.error('خطا در ورود:', error);
        alert(error.message || 'خطایی در ورود به سیستم رخ داد');
    }
});
