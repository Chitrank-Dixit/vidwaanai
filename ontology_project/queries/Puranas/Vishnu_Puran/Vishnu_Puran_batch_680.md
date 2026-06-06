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

### Verse 1 (Vishnu Puran 0.13581)
- **Original**: आता... श्र सततरैध च त़स्वी सतत्पर्द मग्ाम्‌ सकसा मैश्वदेवारते डे > 28 > >> ल्‍ > कर 8 «के बरस » 0 क8 «उस 20 तू लव बन िदकसल ब «8 न. 08 + >्ग्पूह « व 220 0 है श3े 33: .. 28 # 7 8 «8 # हे 2756
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13582)
- **Original**: 35% हैं #0. #4< हक) न्ख्त #>
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13583)
- **Original**: झत्मेकाः सक्मादाय सत्र प्रण्ण इक्तेज सतुसगस्तमपशाततमागेंश सनुत्तगापणोएण रातु परिहत संतुदक्षो महाभागः सतुराजा तया सार्द्टम ऋरत्य कपयाप्फाकमिति सर्व्य गर वदस्येतत्परि्सः सऋणजिदष्यमठमणि0 सक्िदप्यच्युतः . ऋपष्राशिदपि मयास्यमूत> ऋकऋजिएप्यघुता क्राधन्यना रे स्कपप्कसो लाऊ: फ त्यमई हनिश्यापे स स्वेकदा प्रभूलर स लव प्राप्त न सन्‍्देहः पल्वेरच्छ न सत्तपम्‌ स्व असीद परमेरर सत्यो कष्शमिपेक्ष्यामि सददर्श को व्याप्म्‌ आप; अप्याण न 6 रू >> <। 24 7 4 क4<[ 4 का / 4 3 +3 5 “5 7 #स 2, ल्‍7..8 45 +ब नई 4 #े .&ऋ # 4 लीं ही जी आी अं हे 7 2 6 हाई 0 # व ह#ए 0 27 (526) इल्केश , श्लोकाः सददर्श तदा कृशम्‌ सदसद्ूषिणों यत्य सददर्स मुर्नीस्तत्र संद॒दर्ई तमायात्तम्‌ सदानुपहते यज्ने सदावारर्तः प्राज सदेवैरसिंत: कृष्ण: सदेवेशइशरीणणि सम्राष एक पषतः सच्चे वैगुण्यमायात्ति स्देषयायेंद पात्रमू सर्घर्मचारिणों प्राष्य स्तदबदयो ये तु समन्दत्यदयों ये च 329
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13584)
- **Original**: समन्‍दनाएैर्मुनि्भि: 43
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13585)
- **Original**: स निशग्रप्ठतमस्तिष्क: अंड
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13586)
- **Original**: सखतेर्न ममोच्छेद: 38
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13587)
- **Original**: संनत्तानकानामखिलम्‌ 24
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13588)
- **Original**: सल्तोषयामास च तम्‌ 27
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13589)
- **Original**: सन्देशैस्सापपभुरैः 65
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13590)
- **Original**: सच्देदनिर्णयार्थाय इ4
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13591)
- **Original**: सब्याकाले च क्प्माहे 269
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13592)
- **Original**: सव्यासथ्य॑शयोस्तः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13593)
- **Original**: सथ्या रक्रिहो भूमि: 75
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13594)
- **Original**: सन्नहेः सुतीथत्तत्वापि 36 । सन्नतिमरों: कु: #2 46:80 है 7.4 # है 8 4 06 25 सन्निघ्नानाधधाव्ाक्0 <
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13595)
- **Original**: सन्तिपावावधूरैस्तु 33 सन्पाप्नरूपिणेपन्तिल्य॑म्‌ 69
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13596)
- **Original**: स॒र्पपात इतस्तेन 39
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13597)
- **Original**: संपन्नोतनयं दाह / 64
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13598)
- **Original**: सपरः परभ्क्तोताम्‌ 38
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13599)
- **Original**: सपृष्टश मया भूफ 8
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13600)
- **Original**: सआद्रीपानि पाताल" _24
- **Translation**: 

---

