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

### Verse 1 (Sama Ved 0.1981)
- **Original**: 764.प्र सोमासो विपश्चितो5पो नयन्त ऊर्मयः । बनानि महिषा डब
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1982)
- **Original**: जलाशयों में जिम प्रकार लहरें समाहित होती हैं, उसी प्रकार यह ज्ञानवर्द्धध सोमरस जल के साथ मिल जाता है हर
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1983)
- **Original**: 765. अभि द्रोणानि बश्रव: शुक्रा ऋतस्य धारया । वाजं गोमन्तमक्षरन्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1984)
- **Original**: गौदुग्ध रूपी अन्न (पोषक पटार्थ) के साथ भूरे रंग का यह सोपरस जल को धारा के साथ बर्तन में मिलाया जाता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1985)
- **Original**: 766.सुता इन्द्राय वायवे वरुणाय मरूदभ्य: । सोमा अर्घन्तु विष्णवे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1986)
- **Original**: शोधित सोमरस इन्द्र, पवन, मरुतू तथा विष्णु आदि देवगणों को प्राप्त हो
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1987)
- **Original**: उत्तराचिकि ड्वितीयो5ध्याय: 203 767.प्र सोम देववीतये सिन्धुर्न पिप्ये अर्णसा
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1988)
- **Original**: अंशो: पयसा मदिरो न जागृविरच्छा कोशं मधुश्चुतम्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1989)
- **Original**: जल-पूरित नदियों को भाँति हे सोमदेव ! आपको देवगणों के लिए जल में मिलाया जाता है। आप आनन्ददाबी पदार्थों के समान उत्साहवर्द्धक हैं। अत: हे ऋत्विजो ! इस मधुर सोमरस को दूध में मिलाकर पात्र में उत्तम-विधि से भरो
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1990)
- **Original**: 768.आ हर्यतो अर्जुनो अत्के अव्यत प्रिय: सूनुर्न मर्ज्य: । तर्मी हिन्वन्त्यपसो यथा रथं नदीष्वा गभस्त्यो:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1991)
- **Original**: प्रिय शिशु के समान संस्कारित इस स्वच्छ सोमरस को उसी प्रकार वेगपूर्वक हाथों से जल पात्र में घिलाते हैं, जैसे द्रतगामी रथ युद्ध में जाता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1992)
- **Original**: 769.प्र सोमासो मदच्युत: श्रवसे नो मघोनाम्‌। सुता विदथे अक्रमु:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1993)
- **Original**: आनन्दवर्द्ध यह सोम, शोधित होने के बाद यज्ञ में कीर्ति एवं अन्यादि प्रदान करने में सहायक होता
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1994)
- **Original**: 770.आर्दी हंसो यथा गणं विश्वस्यावीवशन्मतिम्‌ । अत्यो न गोभिरज्यते
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1995)
- **Original**: हँस जिस प्रकार (सहज भाव से) अपने समूह में (गतिपूर्वक ) जाता है, उसी गति के साथ यह सोमरस, विवेकवानों की बुद्धि को प्रभावित करता है
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1996)
- **Original**: 7791. आदो त्रितस्य योषणो हरि हिन्वन्त्यद्रिभि: । इन्दुमिन्द्राय पीतये
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1997)
- **Original**: इस शुद्ध हरिद्वर्ण सोम को साधक अपनी अँगुलियों से निचोड़कर इन्द्रदेव के पीने योग्य बनाता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1998)
- **Original**: 772,अया पवस्व देवय, रेभन्यवित्र॑ पर्येणि विश्वत:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1999)
- **Original**: मधोर्धारा असृक्षत
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2000)
- **Original**: हे सोमदेव ! देवगणों से मिलने की इच्छा से शोधित होते समय, अविरल धार के साथ शब्द-नाद करते हुए मधुर होकर, आप प्रचुर मात्रा में स्नवित हों
- **Translation**: 

---

