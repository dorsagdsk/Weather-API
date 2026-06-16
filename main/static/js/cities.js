document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/cities/', {
        method: 'GET',
        headers: {
            'Authorization': 'Token ' + localStorage.getItem('token'),
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch city list.');
        }
        return response.json();
    })
    .then(data => {
        let citiesList = document.getElementById('cityList'); // توجه: اینجا از cityList استفاده شده نه citiesList
        citiesList.innerHTML = '';  // پاک کردن لیست قبلی
        data.forEach(city => {
            let listItem = document.createElement('li');
            listItem.textContent = city.name;
            listItem.onclick = function () {
                fetchWeatherInfo(city.name);
            };
            citiesList.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error(error);
        alert("Failed to retrieve city data.");
    });
});

function fetchWeatherInfo(cityName) {
    fetch('/api/weather/', {
        method: 'POST',
        headers: {
            'Authorization': 'Token ' + localStorage.getItem('token'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name_city: cityName })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch weather data.');
        }
        return response.json();
    })
    .then(data => {
        // نمایش اطلاعات در صفحه به جای استفاده از alert
        document.getElementById('cityName').textContent = cityName;
        document.getElementById('temperature').textContent = data.temperature;

        // نمایش بخش اطلاعات آب و هوا در صورت پنهان بودن
        document.getElementById('weatherInfo').style.display = 'block';
    })
    .catch(error => {
        console.error('Error fetching weather data:', error);
        alert('Failed to fetch weather data for ' + cityName);
    });
}