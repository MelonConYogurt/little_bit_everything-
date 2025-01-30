export interface Book {
  name: string;
  author: string;
  age: number;
  isbn: string;
}

export interface Books {
  data: Book[];
}

export async function getDataBooks(
  name: boolean,
  age: boolean,
  author: boolean,
  isbn: boolean,
  limit: number = 10,
  offset: number = 0
) {
  const url = `http://localhost:8000/books/filter/?limit=${limit}&offset=${offset}&name=${name}&age=${age}&author=${author}&isbn=${isbn}`;
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
