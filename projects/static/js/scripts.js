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

const check_checkboxes = () => { 
    const get_all_checkboxes = document.querySelectorAll('[name="codigo"]')
    const get_delete_project_button = document.getElementById('delete_project_button')
    const get_trash_icon = document.getElementById('trash_icon')

    let cont = 0
    get_all_checkboxes.forEach(element => {
        if(element.checked){
           cont += 1
        }
    }); 
    
    if(cont == 1){
        get_delete_project_button.disabled = false
        get_trash_icon.style.color = "red"
    } else {
        get_delete_project_button.disabled = true
        get_trash_icon.style.color = "grey"
    }
}




