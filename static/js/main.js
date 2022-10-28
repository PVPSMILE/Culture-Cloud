function clickbutton() 
{
    var DESCRIPTION = document.getElementById('DESCRIPTION');
    var button = document.getElementById('BUTTON_DESCRIPTION');
    var dots = document.getElementById('dots');
    if (dots.style.display === 'none'){
        dots.style.display = 'inline';
        button.innerHTML = 'Нажми, если думаешь что Артем полезный';
        DESCRIPTION.style.display = 'none';
    }
    else{
        dots.style.display = 'none';
        button.innerHTML = 'Закрыть';
        DESCRIPTION.style.display = 'inline';
    }
}