export async function getDataBooksSearch(
  limit: number = 10,
  offset: number = 0,
  search: string = ""
) {
  const url = `http://localhost:8000/books/search/?limit=${limit}&offset=${offset}&search=${search}`;
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
