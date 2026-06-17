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

### Verse 1 (Markende Puran 0.2761)
- **Original**: 68--70
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2762)
- **Original**: जो नमस्कार, उनको तमस्कार, उनको बार॑बार नमस्कार
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2763)
- **Original**: >देवताओंदाश देवीकी स्तुति+ 20070574 4547 #+
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2764)
- **Original**: 71--73
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2765)
- **Original**: जौ देवी सब प्राणियोंमें भ्रान्तिरूपसे स्थित हैं, उनको नमस्कार, उनको नमस्कार, डनको बारंबार नमस्कार हैँ
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2766)
- **Original**: जो जीवोंके इन्द्रियवर्गकी अभिप्ताज्ी देबी एवं सब प्राणियोंमें सदा व्याप्त रहनेवाली हैं, उन व्याध्तिदेतीकों बारंबार नमस्कार है
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2767)
- **Original**: जो देवी चैतम्यरूपसे इस सम्पूर्ण जगत्‌कों व्याप्त करके स्थित हैं, उनको नमस्कार, उनको नमस्कार, उनको बारंबार नमस्कार हैं
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2768)
- **Original**: '78--80
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2769)
- **Original**: पूर्वकालमें अपने अभीष्टकी प्राप्ति होनेसे देवताओंने जिनकी स्तुति को तथा देतराज इन्द्रने बहुत दिनोतक जिनका सेवन किया, वह कल्याणकों साधनभूता ईश्वरी हमारा कल्याण और मज्लुल करें तथा सारी आपत्तियोँका नाश कर डाले
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2770)
- **Original**: उह्ण्ड दैत्योंसे सताये हुए हम सभी देवता जिन परमेश्वरीकों इस समय नमस्कार कस्ते हैं तथा जो भक्तिसे विनम्र पुरुषोंद्वाग स्मरण को जानेपर तत्काल हो सम्पूर्ण विपत्तियोंका नाश कर देती हैं, बे जगदाबा हमारा संकट दूर करें
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2771)
- **Original**: ऋषिरुदाच
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2772)
- **Original**: एवं स्तबादियुक्तानां देवानां तन्न पार्वती। स्नरातुप्रभ्यायबौं तोये जाह्ृव्या नृपनन्दन
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2773)
- **Original**: साम्रवीत्तान्‌ सुरान्‌ सुधूर्भवद्धि: स्वूबतेडत्र का शारीरकोशतश्चास्था: समुद्धृतात्॒लीच्छिया
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2774)
- **Original**: स्तोत्र ममतत्‌ क्रियते शुम्भदैल्यनिराकृतैः
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2775)
- **Original**: देव: सपमेतै+ समरे निशुम्भेन पराजित:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2776)
- **Original**: शरीरकोशाघ्यत्तस्था: पार्वत्या निः कौशिकीति समस्तेषु ततो लोकेषु गीयते
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2777)
- **Original**: 'तस्थां बिनिर्गताबां तु कृष्णाभूत्सापिं पार्वती
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2778)
- **Original**: कालिक्रेनि समाख्याता हिमाचललकृताअया
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2779)
- **Original**: ततोअम्बिकां परे रूपे बिज्षाणां सुमनोहरम्‌। ददर्श चण्डो मुण्डश्व भ्रृत्वौ शुम्भनिशुम्भवो;
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2780)
- **Original**: 3, पा0--समझौ: । 207 ताभ्यां शुम्भाय चाख्याता अत्तीस सुमनोहरा
- **Translation**: 

---

