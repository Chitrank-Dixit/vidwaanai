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

### Verse 1 (Garuda1 0.261)
- **Original**: प्रणवेन च लक्ष्यो से गायत्री व गदाधरः। शालग्रामनियासी च शालग्रामस्तथैव चा
- **Translation**: 

---

### Verse 2 (Garuda1 0.262)
- **Original**: जलशायी योगशायी शेषशायी कुशेशय:। महीभर्ता अल कार्य चर कारण पृथिवीधर:
- **Translation**: 

---

### Verse 3 (Garuda1 0.263)
- **Original**: प्रजापति: शाश्वतश्ष काम्य: कामयिता विराट्‌। सप्ताद्‌ पृषा तथा स्वर्गों रशस्थ: सारसशिवलम्‌
- **Translation**: 

---

### Verse 4 (Garuda1 0.264)
- **Original**: धत्री धत्रप्रदों धन्यो यादवातां हिले रतः। अर्जुनस्थ प्रियज्जैव हार्जुनो भीम एव चऊा
- **Translation**: 

---

### Verse 5 (Garuda1 0.265)
- **Original**: पराक्रमो दूर्घियहः सर्वशास्त्रविशारद:
- **Translation**: 

---

### Verse 6 (Garuda1 0.266)
- **Original**: सारस्वतो महाभीष्मः पारिजातहरस्तथा।। अमृतस्य प्रदाता उ्ञ॒ क्षीरोदः क्षीरमेव ऋ्ञ। इन्द्रात्पजस्तस्य गोप्ता गोवर्धनधरस्तथा कंसस्थ नाशनस्तद्वद्धस्तिपों हस्तिनाशन:। शिपिविष्ट:. प्रसलभ्ष॒ सर्वलोकार्तिनाशनः
- **Translation**: 

---

### Verse 7 (Garuda1 0.267)
- **Original**: मुश्े सुद्रा करडय सर्वमुद्राविवर्जित:। देही देहस्थितऔलैव देहस्य च नियामक:
- **Translation**: 

---

### Verse 8 (Garuda1 0.268)
- **Original**: श्ोता श्रोतुतियनता चर ्रोतव्य: अभ्रवर्ण तथा। त्वक्स्घितश्र॒स्पर्शायित्वा स्पृश्यं ज्ञ स्पशँन त्था
- **Translation**: 

---

### Verse 9 (Garuda1 0.269)
- **Original**: रूपद्रष्टा क्ञा चक्षुःस्थो नियन्ता चक्षुपस्तथा। दृश्य॑े चैब तु जिह्मास्थो रसज़श्न नियामकः
- **Translation**: 

---

### Verse 10 (Garuda1 0.270)
- **Original**: प्राणस्थो प्लाणकृद्‌ प्लाता प्राणेन्द्रियनियामक:। काकसश्वो वक्ता लव वक्तत्यो शत्ननं वाइनियामक:
- **Translation**: 

---

### Verse 11 (Garuda1 0.271)
- **Original**: प्राणिस्थ: शिस्पकृषच्छित्पो हस्तयोश्षच॒ तियामक: । प्रदब्यक्ैणगनता ज्ञ॒ गतक्तव्यं गमने तथा
- **Translation**: 

---

### Verse 12 (Garuda1 0.272)
- **Original**: जियलता पादयोशव पाह्धाकू क्र विसर्गकृत। 1-मज़लश्च ब्रुध इति पा0। 2-गजेन्द्रमुखेल0
- **Translation**: 

---

### Verse 13 (Garuda1 0.273)
- **Original**: विसर्गस्थ नियनता उच़॒ ह्ुपस्थस्थ: सुखं तथां
- **Translation**: 

---

### Verse 14 (Garuda1 0.274)
- **Original**: उपस्थस्य वियला थ सदाननदकरअञ हा शत्रुघ्न. कार्त॑वीर्यक्ष॒ दत्तात्रेयस्तथैव च
- **Translation**: 

---

### Verse 15 (Garuda1 0.275)
- **Original**: अलर्कस्प॒ हितक्षव कार्तवीर्षनिकृन्तन:। कालनेप्रिमहानेमिमेंघों मेघपत्तिस्तथा
- **Translation**: 

---

### Verse 16 (Garuda1 0.276)
- **Original**: अनप्रदोडलरूपी ऊ हालादोउऊननप्रवर्तक:
- **Translation**: 

---

### Verse 17 (Garuda1 0.277)
- **Original**: धूपकृद्धूमरूपक्ष उत्तम:
- **Translation**: 

---

### Verse 18 (Garuda1 0.278)
- **Original**: देवक्यानन्दनो नन्‍्दो रोहिण्या: प्रिय एव ल। वसुदेवप्रियज्ैव असुदेवसुतस्तथा
- **Translation**: 

---

### Verse 19 (Garuda1 0.279)
- **Original**: दुस्युभिह्ासरूपक्ष पुष्पहासस्तशैतत च्। अडूह्ासप्रियश्लैव सर्वाध्यक्ष: क्षरो +क्षर:
- **Translation**: 

---

### Verse 20 (Garuda1 0.280)
- **Original**: अच्युतक्षेवसत्येश: सत्यायाक्ष प्रियो बरः। रुक्मिण्याश्न॒पतिश्लैयव. रुक्सिण्या वलल्‍लभस्तथा
- **Translation**: 

---

