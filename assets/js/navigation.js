/**
 * Navigation & Routing Manager for Aviation Examination & Training Platform
 * Handles SPA view switching and hash-based deep linking.
 */
const Navigation = (() => {
  const views = ['home', 'setup', 'exam', 'result', 'paper', 'bank', 'history'];
  let currentView = 'home';

  function init() {
    window.addEventListener('hashchange', handleHashChange);
    // Initial route handling
    if (!window.location.hash) {
      navigateTo('home');
    } else {
      handleHashChange();
    }
  }

  function parseHash() {
    const raw = window.location.hash.replace(/^#/, '');
    const [path, queryStr] = raw.split('?');
    const params = new URLSearchParams(queryStr || '');
    return {
      view: path || 'home',
      params
    };
  }

  function handleHashChange() {
    const { view, params } = parseHash();
    if (views.includes(view)) {
      showView(view, params);
    } else {
      showView('home');
    }
  }

  function navigateTo(viewName, params = {}) {
    const search = new URLSearchParams(params).toString();
    const hash = '#' + viewName + (search ? '?' + search : '');
    if (window.location.hash === hash) {
      handleHashChange();
    } else {
      window.location.hash = hash;
    }
  }

  function showView(viewName, params = new URLSearchParams()) {
    currentView = viewName;
    document.body.dataset.activeView = viewName;

    // Toggle view elements
    views.forEach(v => {
      const el = document.getElementById(`view-${v}`);
      if (el) {
        if (v === viewName) {
          el.removeAttribute('hidden');
          el.classList.add('active-view');
        } else {
          el.setAttribute('hidden', '');
          el.classList.remove('active-view');
        }
      }
    });

    // Update nav links active states
    document.querySelectorAll('[data-nav-view]').forEach(link => {
      const target = link.dataset.navView;
      link.classList.toggle('active', target === viewName);
    });

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Notify App
    if (window.App && window.App.onViewChanged) {
      window.App.onViewChanged(viewName, params);
    }
  }

  function getCurrentView() {
    return currentView;
  }

  return {
    init,
    navigateTo,
    getCurrentView,
    parseHash
  };
})();
