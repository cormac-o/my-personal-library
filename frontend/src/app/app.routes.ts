import { Routes } from '@angular/router';

import { Books } from './components/books/books';
import { Landing } from './components/landing/landing';

export const routes: Routes = [
    { path: '', redirectTo: 'landing', pathMatch: 'full' },
    { path: 'landing', component: Landing },
    { path: 'books', component: Books }
];
