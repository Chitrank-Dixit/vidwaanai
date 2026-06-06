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

### Verse 1 (Markende Puran 0.701)
- **Original**: # कर *
- **Translation**: 

---

### Verse 2 (Markende Puran 0.702)
- **Original**: का का भक का शत 5
- **Translation**: 

---

### Verse 3 (Markende Puran 0.703)
- **Original**: का का 53 के काका 58 क का सुन्दरी ! मुझे पतिन्नता स्त्रियोंके माहात्म्यका सर्वथा
- **Translation**: 

---

### Verse 4 (Markende Puran 0.704)
- **Original**: पुरुपषको कभी नहाँ देखा है, उस सत््यके प्रभावसे आदर करना हैं, इसीलिये तुम्हे मनाती हूँ। यह ब्राह्मग रोगसे मुक्त हो फिरसे तरूण हो जाय पृत्र उदाच और अपनी स्त्रीके साथ सौ बर्षोत्तक जोबित रहे। तथेत्युक्ते तया सूर्यभाजुहाल तपस्विनी।
- **Translation**: 

---

### Verse 5 (Markende Puran 0.705)
- **Original**: यदि भें स्वामीके समान और किसो देवताको नहीं अनसूत्रार््यमुद्यस्थ॒ दशरात्रे क़दा निशि
- **Translation**: 

---

### Verse 6 (Markende Puran 0.706)
- **Original**: समझती तो उस सत्यके प्रभावसे यह ब्राह्मण ततों विबस्वान्‌ भगवान्‌ फुल्लपद्मारुणाकृति:।
- **Translation**: 

---

### Verse 7 (Markende Puran 0.707)
- **Original**: रोगमुक्त होकर पुन: जीवित हो जाय। यदि मन, शैलराजानमुदयमारुरोहोरुमण्डल:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.708)
- **Original**: वाणों एवं क्रियाद्वारा पेरा सारा उद्योग प्रतिदिन समनन्तरमेवास्था भर्ता प्राएँव्ययुज्थत
- **Translation**: 

---

### Verse 9 (Markende Puran 0.709)
- **Original**: स्वामीछी सेवाके ही लिये होता हो तो यह ब्राह्मण पपात अर महीपूृप्ठे पतन्त॑ जगृह़े च स्रा
- **Translation**: 

---

### Verse 10 (Markende Puran 0.710)
- **Original**: जीवित हो जाय। पुत्र ( सुपति ) कहता हैं--ब्राह्मणीके ' तथास्तु '
- **Translation**: 

---

### Verse 11 (Markende Puran 0.711)
- **Original**: हक ए कहकर स्वीकार करनेपर तप॑स्विनों अनसूयाने आर्ध्य द्वाथपमें लेकर सूर्यदेवका आवाहन किया। उस समसयतक दस दिनोंके बराबर गत बीत चुकी थी। तदनन्तर भगवात्‌ सूर्य खिले छुए कमलके समान अरुण आकृति धारण किये अपने महान्‌ पण्डलके साथ गिरिराज उदयाचलपर आऊूढ़ हुए। सूर्वदेवके प्रकट होते ही ब्राह्मणीका पति प्राशहहीन होकर पृथ्जीपर गिरा; किन्तु उसकी पत्लीने गिरते समय उसे पकड़ लिया। अनबूकोवाच न बिवादस्त्तया भद्दे कर्तव्यः पश्य मे बलप्‌। पतिशुअ्रूघयावाप्त त्पसः कि चिरेण ते
- **Translation**: 

---

### Verse 12 (Markende Puran 0.712)
- **Original**: यथा भर्तसप्ं॑ नान्यमपश्यं पुरुष क्न्षित्‌। रूपतः शीलतो युय्द्या बाइस्माधुर्वादिभूषणीः
- **Translation**: 

---

### Verse 13 (Markende Puran 0.713)
- **Original**: त्तेन सत्वेन विप्रोउ्य॑ व्याधिमुक्त: पुनर्युवा। कम प्राप्रोतु जीवित॑ भार्यासहाय: शरदां शत्तम्‌
- **Translation**: 

---

### Verse 14 (Markende Puran 0.714)
- **Original**: यृत्र वाच चथा भर्तृंसम॑ नान्यमह पश्वामसि दैलतम्‌। ततो विप्र: सपुत्तस्थी व्याधिपुक्तः पुनर्युवा। त्ेन सत्येन विप्रोडईयं पुनर्जीवत्वतामयः
- **Translation**: 

---

### Verse 15 (Markende Puran 0.715)
- **Original**: स्वभाभिर्भासबन्‌ वेह्म वृन्दारक इवाजर:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.716)
- **Original**: कर्मणा मनसा खाद्चा भर्तुराराथन प्रत्ति। ततो5पतन्‌ पुष्यबृष्टिदेववाध्यादिनि:स्वनः यथा पमोञ्यमो नित्ये तथाये जीब्ताद द्विज:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.717)
- **Original**: लेधिरे चर मु्दं देजा अनसूग्मामथाब्रुबन्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.718)
- **Original**: अनसूया ब्रोलीं-- भद्गे ! तुम विपाद न करना ।
- **Translation**: 

---

### Verse 19 (Markende Puran 0.719)
- **Original**: पुत्र कहता है--पित्ताजो
- **Translation**: 

---

### Verse 20 (Markende Puran 0.720)
- **Original**: अनसूयादेवी के इंसना पत्तिकी सेवासे जो तपोबल मुझे प्रात हुआ है, उसे
- **Translation**: 

---

