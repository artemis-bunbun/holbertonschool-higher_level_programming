#!/usr/bin/node
document.getElementById('add_item').addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('ul.my_list').appendChild(li);
});
