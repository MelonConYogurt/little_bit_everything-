export interface Book {
  name: string;
  author: string;
  age: number;
  isbn: string;
}

export interface Books {
  data: Book[];
}

export async function getDataBooks() {
  const url = "http://127.0.0.1:8000/books/";
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
