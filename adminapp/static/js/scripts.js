function onAddUserHandler() {
    const user = createUser();
    users.push(user);
    renderUsersToTable();#TO BE CONTINUED!!!!
    document.getElementById('new_user_form').reset();
}

function onKissVadimkaHandler(position) {
    users.splice(position, 1);
    renderUsersToTable();
}

function createUser() {
    return  {
        firstName: document.getElementById('FirstName').value,
        lastName: document.getElementById('LastName').value,
        phone: document.getElementById('Tel').value,
    };
}

function createBook() {
    return  {
        title: document.getElementById('Title').value,
        author: document.getElementById('Author').value,
    };
}

function onAddBookHandler() {
    const book = createBook();
    books.push(book);
    renderBooksToTable();# TO BE CONTINUED
    document.getElementById('new_book_form').reset();
}
