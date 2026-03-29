const navToggle = document.querySelector("[data-nav-toggle]");
const nav = document.querySelector("[data-nav]");

if (navToggle && nav) {
  navToggle.addEventListener("click", () => {
    nav.classList.toggle("is-open");
  });
}

document.querySelectorAll("[data-flash]").forEach((flash) => {
  window.setTimeout(() => {
    flash.style.opacity = "0";
    flash.style.transform = "translateY(-6px)";
    flash.style.transition = "opacity 0.25s ease, transform 0.25s ease";
  }, 4200);
});

const githubRepoSection = document.querySelector("[data-github-repos]");

const githubIconMarkup = `
  <span class="github-icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" role="img" focusable="false">
      <path
        fill="currentColor"
        d="M12 .5C5.65.5.5 5.66.5 12.02c0 5.09 3.3 9.4 7.87 10.93.58.11.79-.25.79-.56 0-.28-.01-1.19-.02-2.15-3.2.7-3.88-1.36-3.88-1.36-.52-1.34-1.28-1.69-1.28-1.69-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.56-.29-5.24-1.29-5.24-5.72 0-1.26.45-2.29 1.18-3.1-.12-.29-.51-1.47.11-3.06 0 0 .97-.31 3.17 1.18A10.94 10.94 0 0 1 12 6.32c.97 0 1.95.13 2.87.38 2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.24 2.77.12 3.06.73.81 1.17 1.84 1.17 3.1 0 4.44-2.69 5.43-5.26 5.72.41.36.78 1.08.78 2.19 0 1.58-.01 2.85-.01 3.24 0 .31.21.68.8.56 4.56-1.53 7.86-5.84 7.86-10.93C23.5 5.66 18.35.5 12 .5Z"
      />
    </svg>
  </span>
`;

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function renderGithubFallback(container, profileUrl) {
  container.innerHTML = `
    <article class="card product-card github-card">
      <div class="card-topline">GitHub / Fallback</div>
      <h3>GitHub API unavailable</h3>
      <p>Please open my GitHub profile directly to browse the full project list.</p>
      <div class="card-footer">
        <span class="github-meta">Profile</span>
        <a class="button button-secondary button-small" href="${profileUrl}" target="_blank" rel="noopener noreferrer">
          ${githubIconMarkup}
          <span>View GitHub</span>
        </a>
      </div>
    </article>
  `;
}

function renderGithubRepos(container, repos, profileUrl) {
  container.innerHTML = repos
    .map((repo, index) => {
      const description = repo.description
        ? escapeHtml(repo.description)
        : "No description provided for this repository.";

      return `
        <article class="card product-card github-card">
          <div class="card-topline">GitHub / ${String(index + 1).padStart(2, "0")}</div>
          <h3>${escapeHtml(repo.name)}</h3>
          <p>${description}</p>
          <div class="card-footer">
            <span class="github-meta">Repository</span>
            <a class="button button-secondary button-small" href="${repo.html_url}" target="_blank" rel="noopener noreferrer">
              ${githubIconMarkup}
              <span>View GitHub</span>
            </a>
          </div>
        </article>
      `;
    })
    .join("");

  if (!repos.length) {
    renderGithubFallback(container, profileUrl);
  }
}

async function loadGithubRepos() {
  if (!githubRepoSection) {
    return;
  }

  const username = githubRepoSection.dataset.githubUsername;
  const profileUrl = githubRepoSection.dataset.githubProfileUrl;
  const repoLimit = Number(githubRepoSection.dataset.repoLimit || "3");

  if (!username || !profileUrl) {
    return;
  }

  try {
    const response = await fetch(
      `https://api.github.com/users/${encodeURIComponent(username)}/repos?sort=updated&per_page=${repoLimit}`,
      {
        headers: {
          Accept: "application/vnd.github+json",
        },
      },
    );

    if (!response.ok) {
      throw new Error(`GitHub API request failed with status ${response.status}`);
    }

    const repos = await response.json();
    const normalizedRepos = Array.isArray(repos)
      ? repos
          .filter((repo) => repo && repo.html_url && repo.name)
          .slice(0, repoLimit)
      : [];

    renderGithubRepos(githubRepoSection, normalizedRepos, profileUrl);
  } catch (error) {
    console.error("Failed to load GitHub repositories:", error);
    renderGithubFallback(githubRepoSection, profileUrl);
  }
}

loadGithubRepos();
