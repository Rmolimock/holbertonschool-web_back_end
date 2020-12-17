import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([
    uploadPhoto(),
    createUser(),
  ]).then((proms) => {
    console.log(proms[0].body, proms[1].firstName, proms[1].lastName);
  }, () => console.log('Signup system offline'));
}
