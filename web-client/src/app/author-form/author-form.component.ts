import { Component, OnInit } from '@angular/core';
import { Author } from '../author';

@Component({
  selector: 'app-author-form',
  templateUrl: './author-form.component.html',
  styleUrls: ['./author-form.component.css']
})
export class AuthorFormComponent implements OnInit {
  model: Author = new Author();

  constructor() { }

  ngOnInit(): void {
  }
}
