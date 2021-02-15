export class Author {
  constructor(
      public id?: number,
      public names: string[] = [],
      public surnames: string[] = [],
      public pseudonym: string = ""
  ) {}
}