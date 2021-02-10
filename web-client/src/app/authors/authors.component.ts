import { Component, OnInit } from '@angular/core';
import { Author } from '../author';

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.css']
})
export class AuthorsComponent implements OnInit {

  authors: Author[] = [
    { id : 1, names : ['Brandon'], surnames : ['Sanderson'] },
    { id : 2, names : ['John', 'Ronald', 'Reuel'], surnames : ['Tolkien'] }
  ];

  get_long_name(author: Author): string {
    if (author.pseudonym) {
      return author.pseudonym;
    }
    return author.names.join(' ') + ' ' + author.surnames.join(' ')
  }

  constructor() { }

  ngOnInit(): void {
  }
}
