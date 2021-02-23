import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EmailsComponent } from './emails/emails.component';
import { EventsComponent } from './events/events.component';
import { OrganizationsComponent } from './organizations/organizations.component';
import { SettingsComponent } from './settings/settings.component';

const routes: Routes = [
  {path: 'Organizations', component: OrganizationsComponent},
  {path: 'Events', component: EventsComponent},
  {path: 'Emails', component: EmailsComponent},
  {path: 'Settings', component: SettingsComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
