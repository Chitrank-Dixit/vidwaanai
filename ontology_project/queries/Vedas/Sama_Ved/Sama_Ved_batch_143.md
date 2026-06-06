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

### Verse 1 (Sama Ved 0.2841)
- **Original**: 1100.अयं॑ दक्षाय साधनो5यं शर्धाय बीतये । अयं देवेभ्यो मधुमत्तर: सुतः
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2842)
- **Original**: बलवृद्धि के साधनरूप इस मधुरतम सोमरस को देवताओं के पीने हेतु विधिवत्‌ निकालते हैं । वे शक्ति- सामर्थ्यवान्‌ बनने के लिए इसका पान करते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2843)
- **Original**: 1101.सोमा: पवन्त इन्दवो स्मभ्यं गातुवित्तमा: ।मित्रा: स्वाना अरेपस: स्वाध्यः स्वर्विंद:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2844)
- **Original**: मित्र के सदृश हितैषी, ख़बित हुए, पापरहित और श्रेष्ठ उद्देश्य के प्रेरक, आत्मतत्त्वदर्शी, स्तुति योग्य, दीप्तिमान्‌ सोमरस हमारे लिए पात्र में पवित्र होता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2845)
- **Original**: 1102.ते पूतासो विपश्चित: सोमासो दध्याशिर: । सूरासो न दर्शतासो जिगत्लवो घ्रुवा घते
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2846)
- **Original**: उत्तरा्िके सप्तमो5ध्याय: 7.9 देखने में सूर्यदेव के सदूश तेजस्वी, शुद्ध, विलक्षण सोम दधि से युक्त कलश में स्थिर है । बह जल की स्निग्ध धार से मिलकर पचित्र होने वाला है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2847)
- **Original**: 1103.सुष्वाणासो व्यद्विभिश्चिताना गोरधि त्वचि
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2848)
- **Original**: इषमस्मभ्यमभित: समस्वरन्वसुविद:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2849)
- **Original**: पृथ्वी के ऊपर निवास करने वाला, अनेक पत्थरों से पिसने वाला, धनदायक सोम, हमें प्रचुर मात्रा में घन प्रदान करता है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2850)
- **Original**: 1104. अया पवा पवस्वैना वसूनि मांश्त्व इन्दो सरसि प्र धन्व । ब्रध्मश्चिद्यस्य वातो न जूर्ति पुरुमेधाश्चित्तकवे नरं धात्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2851)
- **Original**: हे सोमदेव ! अपनी इस पावन धारा से आप हमें धन से अभिपूरित करें । हे सोमदेव ! श्रेष्ठ जल में मिश्रित आपका सेवन करके सूर्यदेव भी हवा के समान गतिशील होते हैं। अति ज्ञानवान्‌ इन्द्रदेव सोमपान करके हमें न्ेतृत्त्व- क्षमता सम्पन्न सन्तान प्रदान करते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2852)
- **Original**: 1105. उत न एना पवया पवस्वाधि श्रुते श्रवाय्यस्य तीर्थे । षष्टिं सहस्रा नैगुतो वसूनि वृक्ष न पक्‍व॑ धूनवद्रणाय
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2853)
- **Original**: है सोम !सबके लिए स्तुत्य, आप हमारे यज्ञ में पवित्र धारा के साथ शुद्ध हों । हे शत्रुनाशक ! पेड़ों से मिलने वाले पके फल की भाँति सहस्रों प्रकार का धन शत्रुओं से मुकाबला करने के लिए हमें प्रदान करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2854)
- **Original**: 1106.महीमे अस्य वृष नाम शूषे मांश्वत्वे वा पृशने वा बचत्रे । अस्वापयन्निगुतः स्नेहयच्चापामित्रां अपाचितो अचेत:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2855)
- **Original**: साधकों पर सुखों की दर्षा करना और दुराचारियों को पराजित करके झुकाना-- ये दो आपके सुखदायी कार्य हैं। (है सोम ! आप) संग्राम द्वारा (अस्त्र प्रहार द्वारा) मल्लयुद्ध द्वारा अथवा छुपकर, (काम, क्रोध आदि ।
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2856)
- **Original**: ) हानि पहुँचाने वाले शत्रुओं को शक्तिहीन करके नष्ट करें । जड़ता को (मू्खों को) हमसे दूर करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2857)
- **Original**: इति पषष्ठ: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2858)
- **Original**: क्केके
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2859)
- **Original**: सप्तम: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2860)
- **Original**: 1107. अनने त्वं नो अन्तम उत त्राता शिवो भुवो वरूथ्य:
- **Translation**: 

---

