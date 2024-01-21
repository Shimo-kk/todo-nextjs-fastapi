import Link from "next/link";

export default function Header() {
  return (
    <header className="h-19 w-full items-center justify-between bg-white dark:bg-gray-800 py-2 px-6 flex">
      <Link
        href="/"
        className="inline-flex items-center gap-2.5 text-2xl font-bold text-gray-800 dark:text-white md:text-3xl"
      >
        <svg
          width="95"
          height="94"
          viewBox="0 0 95 94"
          className="h-auto w-6 text-indigo-600"
          fill="currentColor"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M96 0V47L48 94H0V47L48 0H96Z" />
        </svg>
        ToDo
      </Link>

      <div className="-ml-8 flex-col gap-2.5 sm:flex-row sm:justify-center lg:flex lg:justify-start">
        <Link
          href="/auth/signin"
          className="inline-block rounded-lg px-3 py-2 text-center text-sm font-semibold text-gray-400 outline-none ring-indigo-300 transition duration-100 hover:text-indigo-500 focus-visible:ring active:text-indigo-300"
        >
          サインイン
        </Link>

        <Link
          href="/auth/signup"
          className="inline-block rounded-lg bg-indigo-600 dark: px-4 py-2 text-center text-sm font-semibold text-white outline-none ring-indigo-300 transition duration-100 hover:bg-indigo-500 focus-visible:ring active:bg-indigo-300"
        >
          サインアップ
        </Link>
      </div>
    </header>
  );
}
