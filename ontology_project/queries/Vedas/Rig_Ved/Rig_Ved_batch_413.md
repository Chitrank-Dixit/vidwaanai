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

### Verse 1 (Rig Ved 0.8241)
- **Original**: 3583. ता इन्वे3व समना समानीरमीतवर्णा उषसश्चरन्ति । गृहन्तीरभ्वमसितं रुशद्धि: शुक्रास्तनूभि: शुचयों रुचाना:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.8242)
- **Original**: वे उषाएँ एक जैसी रंग-रूप बाली तथा अपरिभित रंगों से सम्पन्न होकर संचरित होती है । वे बिस्तृत तमिस्रा को आच्छादित (निरस्त) कर देती हैं तथा अपने कान्तिपूर्ण शरीरों के द्वारा पवित्र प्रकाश को और भी देदीप्यमान कर देती हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.8243)
- **Original**: 3584. रयिं दिवो दुहितरों विभाती: प्रजावन्तं यच्छतास्मासु देवी: । स्थोनादा यः प्रतिबुध्यमाना: सुवीर्यस्य पतय: स्थाम
- **Translation**: 

---

### Verse 4 (Rig Ved 0.8244)
- **Original**: हे चुलोक की दुहिता उषाओ ! आप च्योतमान्‌ देवियाँ हैं । आप हम लोगों को सन्तानों से युक्त ऐश्वर्य प्रदान करें । हे देवियों ! हम मनुष्य हर्ष प्राप्ति के लिए आपसे निवेदन करते हैं, जिससे हम लोग श्रेष्ठ सन्तानों से युक्त ऐश्वर्य के स्वामी हो सकें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.8245)
- **Original**: 3585, तद्ठो दिवो दुहितरो विभातीरुप ब्रुब उषसो यज्ञकेतु:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.8246)
- **Original**: बय॑ स्थाम यशसो जनेषु तदलद्यौश्व धत्तां पृथिवी च देवी
- **Translation**: 

---

### Verse 7 (Rig Ved 0.8247)
- **Original**: हे प्रकाशमान सूर्य-पुत्री उपाओ ! हम याजक यज्ञ के निदेशक हैं । आपके समीप हम लोग स्तुति करते हैं, जिससे मनुष्यों के बीच में हम लोग यश तथा अन्न के अधिपति हो सकें । हमारी उस कामना को द्यावा-पृथिवी सफल करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8248)
- **Original**: [ सूक्त - 52 ] [ऋषि - वामदेव गौतम । देवता - उषा । छन्द - गायत्री
- **Translation**: 

---

### Verse 9 (Rig Ved 0.8249)
- **Original**: 3586. प्रति ष्या सूनरी जनी व्युच्छन्ती परि स्वसुः
- **Translation**: 

---

### Verse 10 (Rig Ved 0.8250)
- **Original**: दिवो अदर्शि दुहिता
- **Translation**: 

---

### Verse 11 (Rig Ved 0.8251)
- **Original**: सब प्राणियों की प्रेरक, फल प्रदायक, अपनी बहिन के तुल्य ग़त्रि के अन्त में प्रकाश फैलाने वाली सूर्य पुत्री उषा को सब देखते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.8252)
- **Original**: मं0 4 सू0 53 79 3587, अश्वेव चित्रारुषी माता गवामृतावरी । सखाभुदश्चिनोरुषा:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.8253)
- **Original**: चपला(बिजली) के समान अद्भुत दीप्तिमान्‌ किरणों की माता, यज्ञ आरम्भ करने वाली उषा अश्विनीकुमारों को मित्र हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.8254)
- **Original**: अप्िमीकुमार रोगों का उपचार करते हैं, उषा इस कार्य में सहायक है
- **Translation**: 

---

### Verse 15 (Rig Ved 0.8255)
- **Original**: ] 3588, उत सखास्यश्विनोरुत माता गवामसि। उतोषो वस्व ईशिपे
- **Translation**: 

---

### Verse 16 (Rig Ved 0.8256)
- **Original**: आप अश्विनीकुमारों की मित्र हैं और दीप्तिमान्‌ रश्मियों की रचयित्री हैं, इसलिए हे उषा देवि ! आप स्तुति योग्य हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.8257)
- **Original**: 3589, यावयद्‌ द्वेषसं त्वा चिकित्वित्सूनृतावरि । प्रति स्तोमैरभुत्स्महि
- **Translation**: 

---

### Verse 18 (Rig Ved 0.8258)
- **Original**: हे मधुर बोलने वाली उषा देवि ! आप रिपुओं को अलग करने वालो हैं। आप ज्ञान समप्र हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.8259)
- **Original**: स्तुतियों के द्वारा हम आपको जाग्रतू करते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.8260)
- **Original**: 3590. प्रति भद्रा अदृक्षत गवां सर्गा न रश्मय: । ओषा अप्रा उरु ज़य:
- **Translation**: 

---

