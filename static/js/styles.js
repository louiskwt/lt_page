window.onload = () => {
  const headings = document.querySelectorAll("h1");
  console.log(headings);

  const headingClass = ["text-2xl", "font-bold"];

  headings.forEach((heading) => {
    const {classList} = heading;
    headingClass.forEach((className) => {
      if (!classList.contains("text-3xl")) {
        classList.add(className);
      }
    });
  });
};
