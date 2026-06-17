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

### Verse 1 (Rig Ved 0.321)
- **Original**: 144. विश्वेभि: सोम्य॑ मध्वग्न इन्द्रेण वायुना। पिबा मित्रस्य धामभि:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.322)
- **Original**: है अभ्देव ! आप इन्द्र, वायु, पित्र आदि देवों के सम्पूर्ण तेजों के साथ मधुर सोमरस का पान करें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.323)
- **Original**: में0 1 सू0 15 17 145. त्वं होता मनुहिंतो5ग्ने यज्ञेषु सीदसि। सेमं नो अध्वरं यज
- **Translation**: 

---

### Verse 4 (Rig Ved 0.324)
- **Original**: हे मनुष्यों के हितेषी अग्निदेव ! आप होता के रूप में यज्ञ में प्रतिष्ठित हों और हमारे इस हिसारहित यज्ञ को सम्पन्त करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.325)
- **Original**: 146, सुक्ष्या ह्ारुषी रथे हरितो देव रोहित: । ताभिददेंवाँ डहा वह
- **Translation**: 

---

### Verse 6 (Rig Ved 0.326)
- **Original**: है अग्निदिव ! आप रोहित नामक रथ को ले जाने में सक्षम, तेजगति वाली घोड़ियों को रथ में जोतें एवं उनके द्वारा देवताओं को इस यज्ञ में लाएँ
- **Translation**: 

---

### Verse 7 (Rig Ved 0.327)
- **Original**: [ सूक्त - 15 ] [ऋषि - मेधातिधि काण्व । देवता-(प्रतिदेवता ऋतु सहित) 1.5 इन्द्र, 2 मरुद्गण, 3 त्वष्टा, 4, 12 अग्नि, 6 मित्रावरुण, 7, 10 द्रविणोदा, 11 अश्विनीकुमार । छन्द-गायत्री
- **Translation**: 

---

### Verse 8 (Rig Ved 0.328)
- **Original**: ] 147, इन्द्र सोम॑ पिब ऋतुना त्वा विशन्त्विन्दव:। मत्सरासस्तदोकसः
- **Translation**: 

---

### Verse 9 (Rig Ved 0.329)
- **Original**: हे इन्द्रदेव ! ऋतुओं के अनुकूल सोमरस का पान करें, ये सोमरस आपके शरीर में प्रविष्ट हों; क्योंकि आपकी तृप्ति का आश्रयभूत साधन यही सोम है
- **Translation**: 

---

### Verse 10 (Rig Ved 0.330)
- **Original**: 148. मरुतः पिबत ऋतुना पोत्राद यज्ञं पुनीतन
- **Translation**: 

---

### Verse 11 (Rig Ved 0.331)
- **Original**: यूयं हि ष्ठा सुदानव:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.332)
- **Original**: दानियों में श्रेष्ठ हे मकतो ! आप पोता नामक ऋत्विज्‌ के पात्र से ऋतु के अनुकूल सोमरस का पान करें एवं हमारे इस यज्ञ को पवित्रता प्रदान करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.333)
- **Original**: 149. अभि यज्ञ गृणीहि नो ग्नावो नेष्ट: पिब ऋतुना। त्वं हि रलथा असि
- **Translation**: 

---

### Verse 14 (Rig Ved 0.334)
- **Original**: हे त्वष्टादेव ! आप पत्नी सहित हमारे यज्ञ को प्रशंसा करें, ऋतु के अनुकूल सोमरसर का पान करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.335)
- **Original**: आप निश्चय ही रलों को देने वाले हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.336)
- **Original**: 150. अमन देवाँ डहा वह सादया योनिषु त्रिषु। परि भूष पिब ऋतुना
- **Translation**: 

---

### Verse 17 (Rig Ved 0.337)
- **Original**: हे अग्निदिव ! आप देवों को यहाँ बुलाकर उन्हें यज्ञ के तीनों सबनों (प्रात, माध्यन्दिन एवं साये) में आसौन करें । उन्हें विभूषित करके ऋतु के अनुकूल सोम का पान करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.338)
- **Original**: 151. ब्राह्मणादिन्द्र राधस: पिबा सोममृतूँरनु । तवेद्धि सख्यमस्तृतम्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.339)
- **Original**: हे इन्द्रदेव ! आप ब्रह्मा को जानने वाले साधक के पात्र से सोमरस का पान करें, क्योंकि उनके साथ आपकी अविच्छिन (अदूट) मित्रता है
- **Translation**: 

---

### Verse 20 (Rig Ved 0.340)
- **Original**: 152. युवं दक्ष धृतत्नत मित्रावरुण दृछठभम्‌। ऋतुना यज्ञमाशाथे
- **Translation**: 

---

