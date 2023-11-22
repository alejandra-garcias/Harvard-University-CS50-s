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
    .then(emails => {
      const emailsView = document.querySelector('#emails-view');
      emailsView.classList.add('emails-view');

      if (emails.length > 0) {
        emails.forEach(email => {
          const emailDiv = document.createElement('div');
          emailDiv.classList.add('email-preview');
          emailDiv.innerHTML = `
            <p>From: ${email.sender}</p>
            <p>Subject: ${email.subject}</p>
            <p>Body: ${email.body}</p>
          `;

          emailDiv.addEventListener('click', function() {
            let email_id = email.id;
            fetch(`/emails/${email_id}`)
            .then(response => response.json())
            .then (email =>{
              // Clear the emailsView
              emailsView.innerHTML = '';

              const innerEmail = document.createElement('div');
              innerEmail.classList.add('inner-email');
              innerEmail.innerHTML=
              `<p>From: ${email.sender}</p>
              <p>Subject: ${email.subject}</p>
              <p>Body: ${email.body}</p>`;
              
              emailsView.appendChild(innerEmail);

            })
            console.log('Aquí haré la lógica para entrar al mensaje!');
          });

          emailsView.appendChild(emailDiv);
        });
      } else {
        const emptyElement = document.createElement('div');
        emptyElement.innerHTML = 'No hay emails para mostrar';
        emptyElement.addEventListener('click', function() {
          console.log('This empty element has been clicked!');
        });
        emailsView.appendChild(emptyElement);
      }
    });

  return false;
}