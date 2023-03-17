using System.Text;
using Trivia;

namespace Tests
{
    internal class ConsoleSpy : IConsole
    {
        public string Content => _output.ToString();

        private readonly StringBuilder _output = new();

        /// <inheritdoc />
        public void WriteLine(string message)
        {
            _output.AppendLine(message);
        }
    }
}
