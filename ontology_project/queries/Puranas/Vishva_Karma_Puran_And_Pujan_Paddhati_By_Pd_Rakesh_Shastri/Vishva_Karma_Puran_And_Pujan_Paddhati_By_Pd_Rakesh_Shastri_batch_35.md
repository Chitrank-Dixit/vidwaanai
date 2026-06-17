# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.681)
- **Original**: रू शांति: शांति: शांति:
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.682)
- **Original**: विश्वकर्मा सूक्त ( मूल ) य इमा विश्वाकभुनानि जाहुवट्घिहोंता न्यसीदत्पिता नमः । स आशिषा द्रविणमिच्छमानः प्रथमच्छदंबरां र आविसेस
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.683)
- **Original**: कि स्विदासीदधिष्ठान मारंभणं उनमस्वित्कथा सीतू । यतो भूमि जनयन्विश्वकर्मा विद्यामोर्थोनमहिमा विश्वचक्षा:
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.684)
- **Original**: विश्वतश्चक्षु ऋत विश्वतो मुखो विश्वततो बाहुरुत विश्वतस्मात्‌ । संबाहुम्यां घमति संपतेत्रघावाभूमि जनयन्देव एकः
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.685)
- **Original**: कि स्विद्नं क उस वृक्ष आस यतो धावा प्रथिनी निष्टतक्षुः । मनीषिणों मनसा प्रच्छतेदुत्तध्यतिष्ठदू भुवनानि घारयन्‌
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.686)
- **Original**: या ते धामनि परमाणि भाडयमा या मध्यमा विश्वकर्माजुतेमा । शिक्षा सखिम्यो हविषि स्वघावः स्वयं यत्रस्व तत्व दूधानः
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.687)
- **Original**: विश्वकर्मन्‌ हविषा वाब्रघानः स्वयं यत्रस्व प्रथिनी मुतधामू
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.688)
- **Original**: मुहयन्त्वन्येडअमितः जनास इहास्माकं मंघधवाँ सूरिरस्तु
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.689)
- **Original**: श्री विश्वकर्मा पुराण एवं पूजन पद्धति 205
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.690)
- **Original**: वाचस्पर्ति विश्वकर्माण मूतये मनोजुब॑ वाजे अधाहुवेमू। सनो पिश्वानि हवनानि जोषद्विशविशभूखसे साधुकर्मा
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.691)
- **Original**: विश्वकर्मन हविषा वर्धनेन जाता रमिन्द्रभकूणो रवध्यमू । तस्मै विशाः समनमन्त पूर्वीरयमुग्रो विहव्यो यप्राउसत्‌
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.692)
- **Original**: चक्षुषः: पिता मनसा हि घीरो घूतमेने अजनन्म्नमाने । यद्वेदन्ता अदृहध्न्तपूर्व आदिधघावा प्रथिवी अप्रथेतामू
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.693)
- **Original**: विश्वकर्मा विमना आसिध्या धाता विधाता परमोततू सन्दक
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.694)
- **Original**: तेषामिष्टानि समिषा मद्रनतियज्ञा सप्तऋषीन पर एक माहुः
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.695)
- **Original**: योनः पिता जनिता यो वधाता धामानि वेद भुवनानि विश्व: । यो देवानां नामघा एमेव तंसम्प्रश्नम्मुवना यन्त्यन्याः
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.696)
- **Original**: त आपजनत द्रवि्ण समस्मा ऋषयः पूर्वे जरितारो न भूना । . असू्ते सूर्ते रजासि निषते ये भूतानि समकृणवन्तिमानि
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.697)
- **Original**: परो दिवा पर एना प्रथिव्या परो देवेभिरसुरैर्यहस्ति । क स्विदू गर्भ प्रथमं दूधदापो यत्र देवा: समपश्यन्त विश्वे
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.698)
- **Original**: तमिदू गर्भ प्रथम दूघदापो यत्र देवाः समगच्छन्न विश्वे । अजस्य नाभावध्ये कमर्पित॑ यस्मिचिश्वानि भुवनानि तस्युः
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.699)
- **Original**: नत॑ विदाथत्र इमा जजानाथ धुष्काकेमन्तरं बभूवं । नीहारेण प्रावृताजलया चा सुतृप उकथशा सश्चरिन्त
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.700)
- **Original**: विश्वकर्मा हाजनिष्ट देव आदि द्रयनधर्वों अभवद्‌ू डितीयः । तृतीयः पिता जानितौषधी नामपां गमभ व्यधात्पुरुन्ना
- **Translation**: 

---

