import React, { useState, useEffect, useMemo } from "react";
import { Check, Zap, Clock, Target, BookOpen, Flame } from "lucide-react";

// ---------- Data ----------
const EXAM_DATE = new Date("2026-11-01T00:00:00");

const SUBJECTS = [
  {
    key: "physics",
    name: "Physics",
    bnName: "পদার্থবিজ্ঞান",
    priority: true,
    hoursPerDay: 2,
    color: "#B23A2E",
    chapters: [
      { id: "p1", name: "ভৌতরাশি ও পরিমাপ" },
      { id: "p2", name: "গতি (Motion)" },
      { id: "p3", name: "বল (Force)" },
      { id: "p4", name: "কাজ, ক্ষমতা ও শক্তি" },
      { id: "p5", name: "পদার্থের অবস্থা ও চাপ" },
      { id: "p6", name: "বস্তুর উপর তাপের প্রভাব" },
      { id: "p7", name: "তরঙ্গ ও শব্দ" },
      { id: "p8", name: "আলোর প্রতিফলন" },
      { id: "p9", name: "আলোর প্রতিসরণ" },
      { id: "p10", name: "স্থির বিদ্যুৎ" },
      { id: "p11", name: "চল বিদ্যুৎ" },
      { id: "p12", name: "বিদ্যুৎ ও চুম্বকত্ব" },
      { id: "p13", name: "জীবন বাঁচাতে পদার্থবিজ্ঞান" },
    ],
  },
  {
    key: "math",
    name: "Math",
    bnName: "গণিত",
    priority: true,
    hoursPerDay: 2,
    color: "#B23A2E",
    chapters: [
      { id: "m1", name: "বাস্তব সংখ্যা" },
      { id: "m2", name: "সেট ও ফাংশন" },
      { id: "m3", name: "বীজগাণিতিক রাশি" },
      { id: "m4", name: "সূচক ও লগারিদম" },
      { id: "m5", name: "এক চলকবিশিষ্ট সমীকরণ" },
      { id: "m6", name: "রেখা, কোণ ও ত্রিভুজ" },
      { id: "m7", name: "ব্যবহারিক জ্যামিতি" },
      { id: "m8", name: "বৃত্ত" },
      { id: "m9", name: "ত্রিকোণমিতিক অনুপাত" },
      { id: "m10", name: "দূরত্ব ও উচ্চতা" },
      { id: "m11", name: "বীজগাণিতিক অনুপাত ও সমানুপাত" },
      { id: "m12", name: "দ্বিঘাত সমীকরণ" },
      { id: "m13", name: "অসমতা" },
      { id: "m14", name: "সসীম ধারা" },
      { id: "m15", name: "পরিমিতি" },
      { id: "m16", name: "পরিসংখ্যান" },
    ],
  },
  {
    key: "biology",
    name: "Biology",
    bnName: "জীববিজ্ঞান",
    priority: false,
    hoursPerDay: 1,
    color: "#1D3557",
    chapters: [
      { id: "b1", name: "জীবন পাঠ" },
      { id: "b2", name: "জীবকোষ ও টিস্যু" },
      { id: "b3", name: "কোষ বিভাজন" },
      { id: "b4", name: "জীবনীশক্তি" },
      { id: "b5", name: "খাদ্য ও পুষ্টি" },
      { id: "b6", name: "পরিবহন" },
      { id: "b7", name: "গ্যাসীয় বিনিময়" },
      { id: "b8", name: "রেচন" },
      { id: "b9", name: "চলন ও অঙ্গচালনা" },
      { id: "b10", name: "সমন্বয়" },
      { id: "b11", name: "জীবের প্রজনন" },
      { id: "b12", name: "বংশগতি ও বিবর্তন" },
    ],
  },
  {
    key: "chemistry",
    name: "Chemistry",
    bnName: "রসায়ন",
    priority: false,
    hoursPerDay: 1,
    color: "#1D3557",
    chapters: [
      { id: "c1", name: "রসায়নের ধারণা" },
      { id: "c2", name: "পদার্থের অবস্থা" },
      { id: "c3", name: "পদার্থের গঠন" },
      { id: "c4", name: "পর্যায় সারণি" },
      { id: "c5", name: "রাসায়নিক বন্ধন" },
      { id: "c6", name: "মোলের ধারণা" },
      { id: "c7", name: "রাসায়নিক বিক্রিয়া" },
      { id: "c8", name: "রসায়ন ও শক্তি" },
      { id: "c9", name: "এসিড-ক্ষারক সমতা" },
      { id: "c10", name: "খনিজ সম্পদ: জীবাশ্ম জ্বালানি" },
      { id: "c11", name: "রসায়ন ও আমাদের জীবন" },
    ],
  },
];

const PHASES = [
  {
    n: 1,
    title: "ভিত্তি ঠিক করা",
    range: "জুলাই – আগস্ট",
    focus:
      "Physics + Math এর দুর্বল চ্যাপ্টারগুলো (গতি, বল, বীজগণিত, জ্যামিতি) থেকে শুরু। প্রতিটা concept ক্লিয়ার না হওয়া পর্যন্ত পরের টপিকে যাবে না।",
  },
  {
    n: 2,
    title: "পুরো সিলেবাস কাভার",
    range: "আগস্ট – সেপ্টেম্বর",
    focus:
      "বাকি সব চ্যাপ্টার শেষ করা — Biology ও Chemistry সহ। প্রতি সপ্তাহে অন্তত ২টা চ্যাপ্টার + আগের পড়া গুলোর MCQ practice।",
  },
  {
    n: 3,
    title: "Practice + Mock Test",
    range: "সেপ্টেম্বর – অক্টোবর",
    focus:
      "Board question + creative question practice। সপ্তাহে ২টা full mock test দিয়ে সময় ধরে exam simulate করা।",
  },
  {
    n: 4,
    title: "ফাইনাল রিভিশন",
    range: "অক্টোবর – নভেম্বর",
    focus:
      "শুধু revision, formula sheet, আগের ভুল প্রশ্নগুলো আবার দেখা। নতুন কিছু ধরা বন্ধ — যা শেখা হয়েছে সেটা pakka করা।",
  },
];

const STORAGE_KEY = "ssc-checklist-v1";

function useCountdown(target) {
  const [now, setNow] = useState(new Date());
  useEffect(() => {
    const t = setInterval(() => setNow(new Date()), 1000 * 30);
    return () => clearInterval(t);
  }, []);
  const diff = Math.max(0, target.getTime() - now.getTime());
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const weeks = Math.floor(days / 7);
  return { days, weeks };
}

function Checkbox({ checked, onClick, color }) {
  return (
    <button
      onClick={onClick}
      aria-label={checked ? "Mark incomplete" : "Mark complete"}
      className="relative w-6 h-6 shrink-0 rounded-[3px] border-2 flex items-center justify-center transition-colors duration-200"
      style={{
        borderColor: checked ? color : "#B7AD8F",
        backgroundColor: checked ? color : "transparent",
      }}
    >
      {checked && <Check size={15} strokeWidth={3.5} className="text-[#F3EEDF]" />}
    </button>
  );
}

export default function App() {
  const { days, weeks } = useCountdown(EXAM_DATE);
  const [checklist, setChecklist] = useState({});
  const [loaded, setLoaded] = useState(false);
  const [activeTab, setActiveTab] = useState("physics");

  useEffect(() => {
    (async () => {
      try {
        const res = await window.storage.get(STORAGE_KEY, false);
        if (res && res.value) setChecklist(JSON.parse(res.value));
      } catch (e) {
        // no saved data yet
      } finally {
        setLoaded(true);
      }
    })();
  }, []);

  useEffect(() => {
    if (!loaded) return;
    window.storage.set(STORAGE_KEY, JSON.stringify(checklist), false).catch(() => {});
  }, [checklist, loaded]);

  const toggle = (id) => {
    setChecklist((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const subjectProgress = (subject) => {
    const total = subject.chapters.length;
    const done = subject.chapters.filter((c) => checklist[c.id]).length;
    return { done, total, pct: total ? Math.round((done / total) * 100) : 0 };
  };

  const overall = useMemo(() => {
    const total = SUBJECTS.reduce((a, s) => a + s.chapters.length, 0);
    const done = SUBJECTS.reduce(
      (a, s) => a + s.chapters.filter((c) => checklist[c.id]).length,
      0
    );
    return { done, total, pct: total ? Math.round((done / total) * 100) : 0 };
  }, [checklist]);

  const totalDailyHours = SUBJECTS.reduce((a, s) => a + s.hoursPerDay, 0);
  const activeSubject = SUBJECTS.find((s) => s.key === activeTab);

  return (
    <div
      className="min-h-screen w-full"
      style={{
        background: "#F3EEDF",
        fontFamily: "'Hind Siliguri', sans-serif",
        color: "#3F3D3A",
      }}
    >
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&family=Baloo+Da+2:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
        .display-font { font-family: 'Baloo Da 2', 'Hind Siliguri', sans-serif; }
        .mono-font { font-family: 'JetBrains Mono', monospace; }
        .ruled-bg {
          background-image: repeating-linear-gradient(
            to bottom,
            transparent,
            transparent 39px,
            #C9BFA5 39px,
            #C9BFA5 40px
          );
        }
        .binder-hole {
          width: 14px;
          height: 14px;
          border-radius: 50%;
          background: #F3EEDF;
          box-shadow: inset 0 2px 3px rgba(0,0,0,0.25);
        }
        @keyframes drawCheck {
          from { stroke-dashoffset: 24; }
          to { stroke-dashoffset: 0; }
        }
        @media (prefers-reduced-motion: reduce) {
          * { animation: none !important; transition: none !important; }
        }
      `}</style>

      <div className="flex">
        {/* Red margin strip with binder holes - signature element */}
        <div
          className="hidden sm:flex flex-col items-center py-8 gap-10 shrink-0"
          style={{ width: "44px", background: "#B23A2E" }}
        >
          {Array.from({ length: 14 }).map((_, i) => (
            <div key={i} className="binder-hole" />
          ))}
        </div>

        <div className="flex-1 relative">
          {/* faint left margin rule line echo on mobile */}
          <div
            className="absolute top-0 bottom-0 left-6 sm:left-10 w-[2px] opacity-40"
            style={{ background: "#B23A2E" }}
          />

          <div className="max-w-5xl mx-auto px-6 sm:px-12 py-10 sm:py-14">
            {/* ---------- HERO ---------- */}
            <header className="mb-10">
              <p
                className="uppercase tracking-[0.25em] text-xs font-semibold mb-3"
                style={{ color: "#B23A2E" }}
              >
                Fahim's SSC Test Exam Mentor
              </p>
              <h1
                className="display-font text-4xl sm:text-6xl font-bold leading-[1.05] mb-4"
                style={{ color: "#1D3557" }}
              >
                পরীক্ষা শুরু হতে
              </h1>

              <div className="flex flex-wrap items-end gap-6 mb-4">
                <div
                  className="inline-flex items-baseline gap-3 px-5 py-3 rounded-lg"
                  style={{
                    background: "#1D3557",
                    color: "#F3EEDF",
                    boxShadow: "3px 3px 0 rgba(178,58,46,0.5)",
                    transform: "rotate(-1.5deg)",
                  }}
                >
                  <span className="mono-font text-5xl sm:text-6xl font-bold">
                    {days}
                  </span>
                  <span className="text-lg font-medium">দিন বাকি</span>
                </div>
                <p className="text-sm sm:text-base max-w-sm" style={{ color: "#4A4A48" }}>
                  ({weeks} সপ্তাহ) — Early November এ Test Exam ধরে হিসাব করা। প্রতিদিন{" "}
                  <span className="font-semibold" style={{ color: "#B23A2E" }}>
                    {totalDailyHours}+ ঘণ্টা
                  </span>{" "}
                  পড়ার প্ল্যান নিচে সাজানো আছে।
                </p>
              </div>
            </header>

            {/* ---------- PRIORITY BANNER ---------- */}
            <section
              className="mb-10 p-5 rounded-lg flex items-start gap-4"
              style={{ background: "#FBF6E9", border: "1px solid #E3D9B8" }}
            >
              <Flame size={26} style={{ color: "#B23A2E" }} className="shrink-0 mt-1" />
              <div>
                <p className="font-semibold text-base mb-1" style={{ color: "#1D3557" }}>
                  এখন সবচেয়ে বড় ফোকাস:{" "}
                  <span
                    style={{
                      background:
                        "linear-gradient(180deg, transparent 65%, #E8B94A 65%)",
                    }}
                  >
                    Physics ও Math
                  </span>
                </p>
                <p className="text-sm" style={{ color: "#4A4A48" }}>
                  তুমি নিজেই বলেছো এই দুইটা এখনো সবচেয়ে দুর্বল জায়গা। তাই এই দুই subject-এ
                  extra সময় (দিনে ২ ঘণ্টা করে) বরাদ্দ রাখা হয়েছে, আর প্রতি সপ্তাহে অন্তত
                  একটা ছোট practice test থাকবে শুধু এই দুইটার MCQ + CQ থেকে।
                </p>
              </div>
            </section>

            {/* ---------- DAILY HOUR BUDGET ---------- */}
            <section className="mb-12">
              <h2
                className="display-font text-2xl font-semibold mb-4 flex items-center gap-2"
                style={{ color: "#1D3557" }}
              >
                <Clock size={22} /> দৈনিক পড়ার বাজেট ({totalDailyHours}+ ঘণ্টা)
              </h2>
              <div className="space-y-3">
                {SUBJECTS.map((s) => (
                  <div key={s.key} className="flex items-center gap-3">
                    <span className="w-24 text-sm font-medium shrink-0">{s.bnName}</span>
                    <div
                      className="flex-1 h-6 rounded-full overflow-hidden"
                      style={{ background: "#E3D9B8" }}
                    >
                      <div
                        className="h-full rounded-full flex items-center justify-end px-2 transition-all duration-500"
                        style={{
                          width: `${(s.hoursPerDay / totalDailyHours) * 100}%`,
                          background: s.color,
                        }}
                      >
                        <span className="mono-font text-xs font-bold text-[#F3EEDF]">
                          {s.hoursPerDay}h
                        </span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
              <p className="text-xs mt-3 italic" style={{ color: "#7A7568" }}>
                * বাকি সময় বিরতি, রিভিশন বা school/coaching-এর কাজে রাখা ভালো।
              </p>
            </section>

            {/* ---------- 4 MONTH PHASE TIMELINE ---------- */}
            <section className="mb-12">
              <h2
                className="display-font text-2xl font-semibold mb-5 flex items-center gap-2"
                style={{ color: "#1D3557" }}
              >
                <Target size={22} /> ৪ মাসের রোডম্যাপ
              </h2>
              <div className="grid sm:grid-cols-2 gap-4">
                {PHASES.map((p) => (
                  <div
                    key={p.n}
                    className="p-5 rounded-lg relative overflow-hidden"
                    style={{ background: "#FBF6E9", border: "1px solid #E3D9B8" }}
                  >
                    <span
                      className="mono-font absolute -top-2 -right-1 text-7xl font-bold opacity-10 select-none"
                      style={{ color: "#1D3557" }}
                    >
                      {p.n}
                    </span>
                    <p className="text-xs font-semibold tracking-wide" style={{ color: "#B23A2E" }}>
                      MONTH {p.n} &middot; {p.range}
                    </p>
                    <h3 className="display-font text-lg font-semibold mt-1 mb-2" style={{ color: "#1D3557" }}>
                      {p.title}
                    </h3>
                    <p className="text-sm relative z-10" style={{ color: "#4A4A48" }}>
                      {p.focus}
                    </p>
                  </div>
                ))}
              </div>
            </section>

            {/* ---------- CHAPTER CHECKLIST ---------- */}
            <section className="mb-8">
              <div className="flex items-center justify-between flex-wrap gap-3 mb-5">
                <h2
                  className="display-font text-2xl font-semibold flex items-center gap-2"
                  style={{ color: "#1D3557" }}
                >
                  <BookOpen size={22} /> চ্যাপ্টার চেকলিস্ট
                </h2>
                <div className="flex items-center gap-2 text-sm">
                  <span className="mono-font font-bold" style={{ color: "#B23A2E" }}>
                    {overall.done}/{overall.total}
                  </span>
                  <span style={{ color: "#7A7568" }}>সম্পন্ন ({overall.pct}%)</span>
                </div>
              </div>

              {/* sticky-note style tabs */}
              <div className="flex flex-wrap gap-2 mb-1">
                {SUBJECTS.map((s) => {
                  const prog = subjectProgress(s);
                  const isActive = activeTab === s.key;
                  return (
                    <button
                      key={s.key}
                      onClick={() => setActiveTab(s.key)}
                      className="px-4 py-2.5 rounded-t-lg text-sm font-semibold transition-all duration-150 relative"
                      style={{
                        background: isActive ? "#FBF6E9" : "#E3D9B8",
                        color: isActive ? s.color : "#7A7568",
                        border: `1px solid ${isActive ? "#E3D9B8" : "transparent"}`,
                        borderBottom: isActive ? "1px solid #FBF6E9" : "none",
                        transform: isActive ? "translateY(1px)" : "none",
                      }}
                    >
                      {s.bnName}
                      {s.priority && (
                        <Zap
                          size={12}
                          className="inline-block ml-1 mb-0.5"
                          style={{ color: isActive ? "#E8B94A" : "#B7AD8F" }}
                          fill={isActive ? "#E8B94A" : "none"}
                        />
                      )}
                      <span className="ml-2 mono-font text-xs opacity-70">
                        {prog.done}/{prog.total}
                      </span>
                    </button>
                  );
                })}
              </div>

              <div
                className="rounded-b-lg rounded-tr-lg p-6 ruled-bg"
                style={{ background: "#FBF6E9", border: "1px solid #E3D9B8" }}
              >
                <div className="space-y-0">
                  {activeSubject.chapters.map((c) => (
                    <div
                      key={c.id}
                      className="flex items-center gap-3 py-[9px]"
                      style={{ height: "40px" }}
                    >
                      <Checkbox
                        checked={!!checklist[c.id]}
                        onClick={() => toggle(c.id)}
                        color={activeSubject.color}
                      />
                      <span
                        className="text-[15px]"
                        style={{
                          color: checklist[c.id] ? "#7A7568" : "#3F3D3A",
                          textDecoration: checklist[c.id] ? "line-through" : "none",
                          textDecorationColor: "#B7AD8F",
                        }}
                      >
                        {c.name}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </section>

            <footer className="text-xs italic pt-4" style={{ color: "#7A7568" }}>
              * চ্যাপ্টারের নাম/ক্রম তোমার বইয়ের সাথে সামান্য এদিক-ওদিক হতে পারে — নিজের বই
              দেখে মিলিয়ে নিও। Progress এখানে সেভ থাকবে, পরে আবার এসে চেক করতে পারবে।
            </footer>
          </div>
        </div>
      </div>
    </div>
  );
}
