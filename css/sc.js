const b = document.querySelector('.topB');
const c = document.querySelector('.topC');
b.classList.remove('fadeInUp');
b.classList.remove('animated');
c.classList.remove('fadeInUp');
c.classList.remove('animated');


const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      b.classList.add('fadeInUp');
      b.classList.add('animated');
      return;
    }

    b.classList.remove('fadeInUp');
    b.classList.remove('animated');
  });

});

observer.observe(document.querySelector('.brands'));