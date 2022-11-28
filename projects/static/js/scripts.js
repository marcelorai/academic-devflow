const filterProjects = () => {

    const buttonFilterProject = document.getElementById('filter_project_button');
    const formFilterProject = document.getElementById('filter_project_form');

    if (buttonFilterProject.classList.contains('disabled')) {
        buttonFilterProject.classList.remove('disabled')
        buttonFilterProject.classList.add('activated')
        formFilterProject.style.display = "block"

    } else if(buttonFilterProject.classList.contains('activated')){
        buttonFilterProject.classList.remove('activated')
        buttonFilterProject.classList.add('disabled')
        formFilterProject.style.display = "none"
    }

}