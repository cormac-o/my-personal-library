import { Component } from '@angular/core';
import { WebService } from '../../services/web-service'; 
import { CommonModule } from '@angular/common';

@Component({
  imports: [CommonModule],
  selector: 'app-books',
  providers: [],
  styleUrl: './books.scss',
  templateUrl: './books.html',
  standalone: true
})
export class Books {

  books_list: any = [];

  page: number = 1;

  constructor(private webService: WebService) {}

  ngOnInit(){
    this.getBooks();
  }

  getBooks() {
    this.webService.getBooks(this.page).subscribe((response: any) => {
      this.books_list = response;
      console.log(this.books_list);
    });
  }
}
