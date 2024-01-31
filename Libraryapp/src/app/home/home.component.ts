import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  isAuthenticated=false;

  constructor(private route:Router){} //dependency injection

  ngOnInit(){
    if('token' in localStorage)
    {
      this.isAuthenticated=true;
    }
    else{
      this.isAuthenticated=false;
    }

  }

  view()
  {
    this.route.navigate(['view'])

  }

  logout(){
    // console.log("before",localStorage.getItem('token'));
    localStorage.clear()
    // console.log("after",localStorage.getItem('token'));
    this.ngOnInit();

  }

}
