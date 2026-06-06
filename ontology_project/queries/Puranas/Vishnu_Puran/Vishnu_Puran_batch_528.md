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

### Verse 1 (Vishnu Puran 0.10541)
- **Original**: कार्यसिद्धिके लिये मनुष्यरूप धारण करनेवाले भगवान्‌ कृष्णने वायुका स्मरण किया और वह उसी समय वहाँ उपस्थित हो गया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10542)
- **Original**: तब्र भगवानने उससे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10543)
- **Original**: आ* 21 ] पक्षम अं 371 गच्छेदं ब्रृहि वायो त्वमलं गर्वेण वासव । दीयतामुग्रसेनाय सुधर्मा भवता सभा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10544)
- **Original**: 14 कृष्णो ब्रबीति राजाईमेतद्रल्लमनुत्तमम्‌ । सुधर्माख्यसभा युक्तमस्यां यदुभिरासितुप्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10545)
- **Original**: 15 श्रीपराझर उकाच इत्युक्त: पवनो गत्वा सर्वमाह शचीपतिम्‌। ददौ सो5पि सुधर्माख्यां सभा वायो: पुरन्दरः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10546)
- **Original**: 16 बायुना चाहतां दिव्यां सभां ते यदुपुड्डवा: । बुभुजुस्सर्वसत्राक्यां गोविन्दभुजसंभ्रया:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10547)
- **Original**: 17 बिदिताखिलविज्ञानो. सर्वज्ञानमयावपि । दिष्याचार्यक्रम॑ वीरौ ख्यापयन्तौ यदूत्तमो
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10548)
- **Original**: 18 ततस्सान्दीपनिं काइयमवन्तिपुरवासिनम्‌ । विद्यार्थ जम्मतुर्बाला कृतोपनयनक्रमौं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10549)
- **Original**: 19 वेदाभ्यासकृतप्रीती. सट्डूर्षणजनार्दनो । तस्य शिष्यत्वमभ्येत्य गुरुवृत्तिपरो हि तौ । दर्शयाझ्नक्रतुर्वीरावाचारमखिले.. जने
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10550)
- **Original**: 20 सरहस्यं घनुर्वेदे ससइग्रहमधीयताम्‌। अहोरात्रचतुष्षष्रणा._ तदद्भधुतमभूदद्विज
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10551)
- **Original**: 21 सान्दीपनिरसम्धाव्य तयो: कर्मातिमानुषम्‌ । विचिन्त्य तौ तदा मेने प्राप्तौ चन्द्रदिवाकरौ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10552)
- **Original**: 22 साज्लांश्व चतुरो बेदान्सर्वशासत्राणि चैव हि । अख्यग्नाममशेष॑ च प्रोक्तमात्रमवाप्य तो
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10553)
- **Original**: 23 ऊचतुर्तब्रियतां या ते दातव्या गुरुदक्षिणा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10554)
- **Original**: 24 सो5प्बतीन्ियमालोक्य तयोः कर्म महामति: । अयाचत मृत पुत्र प्रभासे छवणार्णवे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10555)
- **Original**: 25 गृहीतास्त्रो ततस्तो तु सार््यहस्तो महोदधि: । उवाच्च न गया पुत्रों हतस्सान्दीपनेरिति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10556)
- **Original**: 26 दैत्यः पद्कजनो नाम शब्भरूपस्स बालकम्‌। जग्राह योउस्ति सलिले ममैबासुरसूदन
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10557)
- **Original**: 27 अऔीपराशर उकाच इत्पुक्तो5न्तर्जलं गत्वा हत्वा पच्कजनं च तम्‌ । कृष्णो जग्राह तस्यास्थिप्रभव॑ झल्लमुत्तमम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10558)
- **Original**: 28 कहा--
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10559)
- **Original**: “हे तायो ! तुम जाओ और इच्रसे कहो कि हे वासव ! व्यर्थ गर्व छोड़कर तुम उग्रसेनक्रों अपनी सुधर्मा नामको सभा दो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10560)
- **Original**: कृष्णचन्द्रकी आह्ञा है कि यह सुधर्मा-सभा नामक सर्वोत्तम रत्र ग़जाके ही योग्य है इसमें यादवॉका विराजमान होना उपयुक्त है”
- **Translation**: 

---

