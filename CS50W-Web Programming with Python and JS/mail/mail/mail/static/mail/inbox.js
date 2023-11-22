document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';



  document.querySelector('#compose-submit').addEventListener('click', function(){
      // Retrieving values:
      let compose_recipients = document.querySelector('#compose-recipients').value;
      let compose_subject = document.querySelector('#compose-subject').value;
      let compose_body = document.querySelector('#compose-body').value;

    fetch('/emails',{
      method:'POST',
      body: JSON.stringify({
        
        recipients:compose_recipients,
        subject:compose_subject,
        body:compose_body
  
      }),
  
    })
    .then(response=>response.json())
    .then(result =>{
      console.log(result);
    });
  
    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  });

}
  

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Display the mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails=>{
    console.log(emails)
    // Renderizacion de emails
    if (emails.length > 0){
      const element = document.createElement('div');
      element.innerHTML = 'This is the content of the div.';
      element.addEventListener('click', function() {
      console.log('This element has been clicked!')
      });
      document.querySelector('#emails-view').append(element);
      }
    else{
      const empty_element = document.createElement('div');
      empty_element.innerHTML = 'No hay emails para mostrar';
      empty_element.addEventListener('click', function() {
        console.log('This empty element has been clicked!')
        });
        document.querySelector('#emails-view').append(empty_element);
    }
   
  });
  return false

}