document.addEventListener('DOMContentLoaded', function () {
    const loadMoreBtn = document.getElementById('load-more');
    const articlesContainer = document.getElementById('articles-container');

    loadMoreBtn.addEventListener('click', function () {
      const page = loadMoreBtn.getAttribute('data-page');
      const xhr = new XMLHttpRequest();

      xhr.open('GET', `/load-more-articles/?page=${page}`, true);
      xhr.onload = function () {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          response.posts.forEach(post => {
            const articleDiv = document.createElement('div');
            articleDiv.classList.add('col-lg-6', 'article');
            articleDiv.innerHTML = `
              <article class="card post-card h-100 border-0 bg-transparent">
                <div class="card-body">
                  <a class="d-block" href="/post/${post.slug}" title="${post.title}">
                    <div class="post-image position-relative">
                      <img class="w-100 h-auto rounded" src="/static/images/blog/02.jpg" alt="${post.title}" width="970" height="500">
                    </div>
                  </a>
                  <ul class="card-meta list-inline mb-3">
                    <li class="list-inline-item mt-2">
                      <i class="ti ti-calendar-event"></i>
                      <span>${post.created_at}</span>
                    </li>
                    <li class="list-inline-item mt-2">—</li>
                    <li class="list-inline-item mt-2">
                      <i class="ti ti-clock"></i>
                      <span>2 min read</span>
                    </li>
                  </ul>
                  <a class="d-block" href="/post/${post.slug}" title="${post.title}">
                    <h3 class="mb-3 post-title">${post.title}</h3>
                  </a>
                  <p>${post.excerpt}</p>
                </div>
                <div class="card-footer border-top-0 bg-transparent p-0">
                  <ul class="card-meta list-inline">
                    <li class="list-inline-item mt-2">
                      <img class="w-auto" src="/static/images/author/thomas-macaulay.jpg" alt="${post.author}" width="26" height="26"> by <span>${post.author}</span>
                    </li>
                  </ul>
                </div>
              </article>
            `;
            articlesContainer.appendChild(articleDiv);
          });

          if (!response.has_next) {
            loadMoreBtn.style.display = 'none';
          }

          loadMoreBtn.setAttribute('data-page', parseInt(page) + 1);
        }
      };
      xhr.send();
    });
  });