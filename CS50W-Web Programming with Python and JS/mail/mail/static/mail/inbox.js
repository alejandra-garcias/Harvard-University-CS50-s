document.addEventListener('DOMContentLoaded', function () {
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

  document.querySelector('#compose-submit').addEventListener('click', function () {
    // Retrieving values:
    let compose_recipients = document.querySelector('#compose-recipients').value;
    let compose_subject = document.querySelector('#compose-subject').value;
    let compose_body = document.querySelector('#compose-body').value;

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: compose_recipients,
        subject: compose_subject,
        body: compose_body
      }),
    })
      .then(response => response.json())
      .then(result => {
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
          if(email.read === true && mailbox!='sent'){
            emailDiv.classList.replace('email-preview','read-email');
          }
          emailDiv.innerHTML = `
            <strong>From: ${email.sender}</strong>
            <span class='subject'>Subject: ${email.subject}</span>
            <span>${email.timestamp}</span>
          `;

          emailsView.appendChild(emailDiv);
          // Call display_email for the newly created emailDiv
          display_email(emailDiv, email,emailsView);
        });
      } else {
        const emptyElement = document.createElement('div');
        emptyElement.innerHTML = 'No hay emails para mostrar';
        emptyElement.addEventListener('click', function () {
          console.log('This empty element has been clicked!');
        });
        emailsView.appendChild(emptyElement);
      }
    });

  return false;
}

function display_email(emailDiv, email,emailsView){
  emailDiv.addEventListener('click', function(){
    let email_id = email.id;

    // Mark email as read
    if (email.read !== true){
      fetch(`/emails/${email_id}`, {
        method: 'PUT',
        body: JSON.stringify({
          read: true
        })
      })
        .then(() => {

          console.log('Message marked as read');
        })
        .catch(error => console.error('Error marking message as read:', error));
    } else {
      console.log('The message was already read!');
    }

    // Clear the emailsView to render single email

    emailsView.innerHTML = '';

            const innerEmail = document.createElement('div');
            innerEmail.classList.add('inner-email');
            innerEmail.innerHTML =
            `<div class="innerinner">
            <strong>From:</strong><span> ${email.sender}</span>
            <strong>To:</strong><span> ${email.recipients}</span>
            <strong>Subject:</strong><span> ${email.subject}</span>
            <strong>Timestamp:</strong><span> ${email.timestamp}</span>
            </div>
            <span> ${email.body}</span>`;

             // Archive/Unarchive logic
             const btn_arch = document.createElement('button');
             btn_arch.innerHTML = email.archived ? "Unarchive" : "Archive";
             btn_arch.className = email.archived ? "btn btn-success" : "btn btn-danger";
             btn_arch.addEventListener('click', function () {
               fetch(`/emails/${email_id}`, {
                 method: 'PUT',
                 body: JSON.stringify({
                   archived: !email.archived
                 })
               })
                 .then(() => {
                   load_mailbox('archive');
                 })
                 .catch(error => console.error('Error archiving/unarchiving message:', error));
             });

  // Reply to email
  const reply =  document.createElement('button')
  reply.classList.add('btn-reply');
  reply.innerHTML = "Reply"
  reply.addEventListener('click',function(){
    console.log(email.subject)
    compose_email();
    //Fill in recipients
    document.querySelector('#compose-recipients').value = email.sender
    //Fill in subject
    
    document.querySelector('#compose-subject').value =email.subject.slice(0,4) === "Re: "? email.subject : "Re: " + email.subject;

    //Creating reply body
    const reply_body = `\n\n\n On ${email.timestamp} ${email.sender} wrote: \n \n`;

    document.querySelector('#compose-body').value = reply_body + email.body
    
  })
  innerEmail.appendChild(reply);

  emailsView.appendChild(innerEmail);
  emailsView.appendChild(btn_arch);
});


}