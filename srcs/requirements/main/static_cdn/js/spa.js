document.addEventListener("DOMContentLoaded", function() {
    const contentPage = document.querySelector('#contentPage');
    if (contentPage) {
        if (document.querySelectorAll('a')) {
            document.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', e => {
                    e.preventDefault();
                    const href = link.getAttribute('href');
                    history.pushState({path: href}, '', href);
                    loadPage(href);
                });
            });
        }
    }
    const formElement = document.querySelector('.formElement');
    if (formElement) {
        formElement.addEventListener('submit', function (e) {
            e.preventDefault();
            const formData = new FormData(this);
            fetch(this.action, {
                method: 'POST',
                body: formData,
            }).then(response => response.text()).then(html => {
                const doc = new DOMParser().parseFromString(html, 'text/html');
                const nav = document.querySelector('#navbar_');
                nav.innerHTML = doc.querySelector('#navbar_').innerHTML;
                contentPage.innerHTML = doc.querySelector('#contentPage').innerHTML;
                const title = document.querySelector('#contentPage title');
                if (title) {
                    document.title = title.text;
                    title.remove();
                }
            }).catch(error => console.error('Error:', error));
        });
    }

    window.addEventListener('popstate', function (event) {
        if (history.state && history.state.path) {
            loadPage(history.state.path);
        }
    });

    function loadPage(path) {
        fetch(path,
            {
                redirect: 'follow',
                credentials: 'include',
            }
        )
            .then(response => response.text())
            .then(partHtml => {
                const doc =  new DOMParser().parseFromString(partHtml, 'text/html');
                const nav = document.querySelector('#navbar_');
                nav.innerHTML = doc.querySelector('#navbar_').innerHTML;
                contentPage.innerHTML = doc.querySelector('#contentPage').innerHTML;
                const title = document.querySelector('#contentPage title');
                if (title) {
                    document.title = title.text;
                    title.remove();
                }
            })
            .catch(error => console.error('Error fetching additional part:', error));
    }
});

