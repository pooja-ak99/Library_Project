import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AddComponent } from './add/add.component';
import { ViewComponent } from './view/view.component';
import { LogComponent } from './log/log.component';
import { RegisterComponent } from './register/register.component';
import { DetailComponent } from './detail/detail.component';

const routes: Routes = [
  {path: '',component:HomeComponent},
  {path: 'add',component:AddComponent},
  {path: 'view',component:ViewComponent},
  {path: 'login',component:LogComponent},
  {path: 'register',component:RegisterComponent},
  {path: 'detail/:id',component:DetailComponent},
  {path: 'edit/:id',component:AddComponent},
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
