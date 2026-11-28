import { Routes } from '@angular/router';

import { Books } from './components/books/books';
import { Landing } from './components/landing/landing';
import { Book } from './components/book/book';

export const routes: Routes = [
    { path: '', redirectTo: 'landing', pathMatch: 'full' },
    { path: 'landing', component: Landing },
    { path: 'books', component: Books },
    { path: 'books/:id', component: Book }
];
