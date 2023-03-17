using System;

namespace Trivia
{
    internal class SystemConsole : IConsole
    {
        /// <inheritdoc />
        public void WriteLine(string message)
        {
            Console.WriteLine(message);
        }
    }
}
