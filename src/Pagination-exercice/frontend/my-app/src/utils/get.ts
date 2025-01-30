export interface Book {
  name: string;
  author: string;
  age: number;
  isbn: string;
}

export interface Books {
  data: Book[];
}

export interface Filter {
  name: boolean | null;
  age: boolean | null;
  author: boolean | null;
  isbn: boolean | null;
}

export async function getDataBooks(
  data: Filter,
  limit: number = 10,
  offset: number = 0,
  search: string = ""
) {
  const url =
    `http://localhost:8000/books/filter/?limit=${limit}&offset=${offset}` +
    (search !== "" ? `&search=${search}` : "") +
    (data.name !== null ? `&name=${data.name}` : "") +
    (data.age !== null ? `&age=${data.age}` : "") +
    (data.author !== null ? `&author=${data.author}` : "") +
    (data.isbn !== null ? `&isbn=${data.isbn}` : "");

  try {
    const response = await fetch(url, {
      method: "GET",
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const json = await response.json();
    return json;
  } catch (error) {
    console.log(error);
  }
}
