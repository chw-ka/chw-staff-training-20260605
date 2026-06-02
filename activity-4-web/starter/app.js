const form = document.getElementById('form');
const resetBtn = document.getElementById('reset');
const copyBtn = document.getElementById('copy');

const studentName = document.getElementById('studentName');
const subject = document.getElementById('subject');
const original = document.getElementById('original');
const prefix = document.getElementById('prefix');

const result = document.getElementById('result');
const hint = document.getElementById('hint');

function getExt(filename) {
  const i = filename.lastIndexOf('.');
  if (i === -1) return '';
  return filename.slice(i);
}

function sanitize(s) {
  return String(s).trim().replace(/\s+/g, ' ');
}

function buildName({prefix, student, subject, original}) {
  const ext = getExt(original);
  const p = sanitize(prefix);
  const st = sanitize(student);
  const sub = sanitize(subject);
  return `${p}_${st}_${sub}${ext}`;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const next = buildName({
    prefix: prefix.value,
    student: studentName.value,
    subject: subject.value,
    original: original.value,
  });

  result.textContent = next;
  copyBtn.disabled = false;
  hint.textContent = '已生成。你可以複製檔名，再示範「Drive 整理」或「本地整理」。';
});

resetBtn.addEventListener('click', () => {
  studentName.value = '';
  subject.value = '';
  original.value = '';
  prefix.value = '【功課】';
  result.textContent = '—';
  copyBtn.disabled = true;
  hint.textContent = '提示：呢個 demo 用嚟教「Agent 生成靜態網頁」同基本 JS 事件處理。';
  studentName.focus();
});

copyBtn.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(result.textContent);
    hint.textContent = '已複製到剪貼簿。';
  } catch {
    hint.textContent = '複製失敗：你可以手動選取上面建議檔名。';
  }
});
