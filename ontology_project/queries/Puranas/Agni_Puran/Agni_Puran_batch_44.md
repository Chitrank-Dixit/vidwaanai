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

### Verse 1 (Agni Puran 0.861)
- **Original**: लेता है'
- **Translation**: 

---

### Verse 2 (Agni Puran 0.862)
- **Original**: 13--15
- **Translation**: 

---

### Verse 3 (Agni Puran 0.863)
- **Original**: इस प्रकार आदि आग्रेव महापुदाणमें 'श्रीहतिकी चाँबीस यूर्तियोंके स्तोश्नका वर्णन” नामक अड़तालीसवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 4 (Agni Puran 0.864)
- **Original**: >30000#9::7927........ उनचासवाँ अध्याय मत्स्यादि दशावतारोंकी प्रतिमाओंके लक्षणोंका वर्णन भगवान्‌ हयग्रीव कहते हैं-- ब्रह्मन्‌! अब मैं
- **Translation**: 

---

### Verse 5 (Agni Puran 0.865)
- **Original**: के आकारकी होनी चाहिये। पृथ्वीके उद्धारक तुम्हें मत्स्य आदि दस अवतार-विग्रहोंका लक्षण
- **Translation**: 

---

### Verse 6 (Agni Puran 0.866)
- **Original**: भगवान्‌ बराहको मनुष्याकार बनाना चाहिये, वे बताता हूँ। मत्स्यभगवानूकी आकृति मत्स्यके
- **Translation**: 

---

### Verse 7 (Agni Puran 0.867)
- **Original**: दाहिने हाथमें गदा और चक्र धारण करते हैं। समान और कूर्म भगवान्‌की प्रतिमा कूर्म (कच्छप)-
- **Translation**: 

---

### Verse 8 (Agni Puran 0.868)
- **Original**: उनके बायें हाथमें शद्बु और पद्म शोभा पाते हैं। 1. तात्पर्य यह है कि वासुदैवसे केशव, नारायण और माधयकी, संकर्षणसे गोविन्द, विष्णु और मधुसूदनकौ, प्रद्मुम्रसे ज़िविक्रम, वामत और श्रौधरकी तथा अनिरुद्धसे हपोकेश, पद्मनाभ एवं दामोदरको अभिव्यक्ति हुई। 2. इस अध्यायमें बारह सलोक स्तुतिके हैं। प्रत्येक सलोकमें भगवान्‌कौ दो-दो मूर्तियोंका स्तयन हुआ तथा इन बाएहों श्लोकोंके आदिका एक-एक अक्षर जोड़नेसे ' 3 नमो भगवते वासुदेवाय' यह द्वादशाक्षर मन्र बत्रता है। इसौलिये इसे द्वादशाक्षर-स्तोज एवं चौबोस मूर्तियोंका स्तोत्र कहते हैं। ब्ोभगवानुवाच 3>रूप: केशव: पफ्शब्जुचक्रादाधर:। नारायण: शक्बुपक्मगदाचक्रों प्रदक्षिणम्‌
- **Translation**: 

---

### Verse 9 (Agni Puran 0.869)
- **Original**: उतो गंदी भाधवो5रिशक्लुपक्षी नमामि तम्‌
- **Translation**: 

---

### Verse 10 (Agni Puran 0.870)
- **Original**: चक्रकौमोदकौपदाशद्भी गोविन्द ऊर्शित:
- **Translation**: 

---

### Verse 11 (Agni Puran 0.871)
- **Original**: मौक्षद: क्रोगदी पद्यो श्वी विष्णु चक्रधूक । शब्बुचक्राव्जगदित॑ मधुसूदतमानमे
- **Translation**: 

---

### Verse 12 (Agni Puran 0.872)
- **Original**: अकत्या त्रिविक्रम: पद्ययदी चक्री च॑ शइख्यपि । शब्गुघक्रगदापचौ वामनः पातु मां सदा डे
- **Translation**: 

---

### Verse 13 (Agni Puran 0.873)
- **Original**: गतिद: ओऔधर: पथ्ञो अक्रजाज्री च शबड्ख्यपि
- **Translation**: 

---

### Verse 14 (Agni Puran 0.874)
- **Original**: हपीकेशो गदी चक्रो पत्तों शद्धी च पातु न:
- **Translation**: 

---

### Verse 15 (Agni Puran 0.875)
- **Original**: 5 # अरदः पद्चनाभस्तु शब्बाब्जारिगदाघर: । दामोदर: पण्शद्वुग॒दाचक्री नमामि तम्‌
- **Translation**: 

---

### Verse 16 (Agni Puran 0.876)
- **Original**: तेने गदी शक्बुधक्रों वासुदेवोउम्जभूजगत्‌ । संकर्षणो गदी शक्बे पद्मी चक्रों चपातु व:
- **Translation**: 

---

### Verse 17 (Agni Puran 0.877)
- **Original**: सदी चक्री श्घ॒गदी प्रधुप्तः पद्मभृत्मधु:। अभिरद्धसक्रदी शद्धं पद्चों थ पातु न: 8
- **Translation**: 

---

### Verse 18 (Agni Puran 0.878)
- **Original**: सुरेशोउर्यव्जशब्ञादयः श्रीगदी पुरुषोत्तम: । अधोक्षज: पद्मगदी शद्बुचक्रों च पातु व:
- **Translation**: 

---

### Verse 19 (Agni Puran 0.879)
- **Original**: देयो नृसिंहक्षक्रा्जदी शवों नमामि तम्‌ । अच्युत: श्रीगदी प्ती चक्री शद्धी च पातु व:
- **Translation**: 

---

### Verse 20 (Agni Puran 0.880)
- **Original**: आलरूपी शद्गगदी उपेन्द्रक्षक्रपद्स्यपि । जनादन: पद्चचक्री शद्गुधारी गदाधर:
- **Translation**: 

---

