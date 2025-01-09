document.querySelectorAll('.sidebar a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();  // Prevent the default anchor link behavior
        const targetId = this.getAttribute('href');  // Get the href attribute of the clicked link
        const targetSection = document.querySelector(targetId);  // Select the target section in the document

        // Use the scrollIntoView method for smooth scrolling to the section
        targetSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});
