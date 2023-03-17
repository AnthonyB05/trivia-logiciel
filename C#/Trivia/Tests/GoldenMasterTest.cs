using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;
using Trivia;
using Xunit;

namespace Tests
{
    public class GoldenMasterTest
    {
        [Fact(Skip = "Golden Master")]
        public void RecordEmptyGame()
        {
            var consoleSpy = new ConsoleSpy();
            var game = new Game(consoleSpy);

            var recordedContent = consoleSpy.Content;
            File.WriteAllText(@"C:\Users\kryza\Downloads\GoldenMaster\record.txt", recordedContent);
        }

        private void PlayAGame(Game game, int randomSeed, params string[] players)
        {
            foreach (var player in players)
            {
                game.Add(player);
            }

            var rand = new Random(randomSeed);
            bool notAWinner;

            do
            {
                game.Roll(rand.Next(5) + 1);

                if (rand.Next(9) == 7)
                {
                    notAWinner = game.WrongAnswer();
                }
                else
                {
                    notAWinner = game.WasCorrectlyAnswered();
                }
            } while (notAWinner);
        }

        private string CreateFileName(int randomSeed, params string[] players)
        {
            var fileName = "record-" + randomSeed + '-' + string.Join("-", players) + ".txt";
            return Path.Combine(@"C:\Users\kryza\Downloads\GoldenMaster", fileName);
        }

        [Theory(
            Skip = "Golden Master"
        )]
        [InlineData(0)]
        [InlineData(0, "Chet")]
        [InlineData(0, "Chet", "Pat")]
        [InlineData(0, "Chet", "Pat", "Sue")]
        [InlineData(1, "Chet", "Pat", "Sue")]
        public void RecordPlayedGame(int randomSeed, params string[] players)
        {
            var consoleSpy = new ConsoleSpy();
            var game = new Game(consoleSpy);

            try
            {
                PlayAGame(game, randomSeed, players);
                var recordedContent = consoleSpy.Content;
                File.WriteAllText(CreateFileName(randomSeed, players), recordedContent);
            } 
            catch (Exception e)
            {
                var contentToWrite = new StringBuilder();
                contentToWrite.AppendLine(consoleSpy.Content);
                contentToWrite.AppendLine(e.Message);
                contentToWrite.AppendLine(e.GetType().FullName);
                File.WriteAllText(CreateFileName(randomSeed, players), contentToWrite.ToString());
            }
        }

        [Fact]
        public void ReplayEmptyGame()
        {
            var consoleSpy = new ConsoleSpy();
            var game = new Game(consoleSpy);

            var recordedContent = consoleSpy.Content;
            var expectedContent = File.ReadAllText(@"C:\Users\kryza\Downloads\GoldenMaster\record.txt");

            Assert.Equal(expectedContent, recordedContent);
        }

        [Theory]
        [InlineData(0)]
        [InlineData(0, "Chet")]
        [InlineData(0, "Chet", "Pat")]
        [InlineData(0, "Chet", "Pat", "Sue")]
        [InlineData(1, "Chet", "Pat", "Sue")]
        public void ReplayPlayedGame(int randomSeed, params string[] players)
        {
            var consoleSpy = new ConsoleSpy();
            var game = new Game(consoleSpy);

            string recordedContent;

            try
            {
                PlayAGame(game, randomSeed, players);
                recordedContent = consoleSpy.Content;
            }
            catch (Exception e)
            {
                var contentToWrite = new StringBuilder();
                contentToWrite.AppendLine(consoleSpy.Content);
                contentToWrite.AppendLine(e.Message);
                contentToWrite.AppendLine(e.GetType().FullName);
                recordedContent = contentToWrite.ToString();
            }

            var expectedContent = File.ReadAllText(CreateFileName(randomSeed, players));
            Assert.Equal(expectedContent, recordedContent);
        }
    }
}
