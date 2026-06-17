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

### Verse 1 (Vishnu Puran 0.7581)
- **Original**: भायां पुरोह्िितश्चैणसेनानी रथकृध यः । फ्ल्यश्चकलभाश्रेति प्राणिन: सप्त कीर्तिता:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7582)
- **Original**: चतुर्दशेति रज्ाति सर्वेषों चक्रवर्ितान्‌ ।' अर्थात्‌ चक्र, रथ, मणि, खड़, चर्म (ढाल), ध्वजा और निधि (खजाना) थे सात प्राणहीन तथा रत्नी, प्रोष्ित, सेनापति, रखी, पदाति. अद्याग्रेही और गकरोहो--ये सात प्राणयूक्त इस फ्रघर कुछ चोदह रख सब चक्सर्नियोंके यहाँ रहते हैं ।
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7583)
- **Original**: आ0 12 ] चतुर्थ अंश 269 तथ्ारिचक्रमपास्तपुत्रकल्त्रबन्धुबलकोरा स्वपधिष्ठान॑ परित्यज्य दिश: प्रति विद्युतम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7584)
- **Original**: तस्मंश्व॒ बिद्वुतेकतित्रासलोलायत- लोचनयुगलं त्राहि त्राहि मां ताताम्ब श्रात- रित्याकुलविलापबिधुरं स राजकन्यारत्रमद्राक्षीत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7585)
- **Original**: तहर्शनाश्च तप्यामनुरागानुगतान्तरात्मा स॒ नृपो5चिन्तयत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7586)
- **Original**: साध्विदं ममापत्य- रहितस्थ वन्ध्याभर्तु: साम्प्रत॑ विधिनापत्यकारणं कन्यारत्रमुपपादितम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7587)
- **Original**: तदेतत्समुद्रहामीति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7588)
- **Original**: अथयवैनां स्वन्दनमारोप्य स्वमधिष्ठानं नयामि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7589)
- **Original**: तयैव देव्या शैव्यवाहमनुज्ञात- स्समुद्दद्रामीति । 22
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7590)
- **Original**: अथैनां रथमारोप्य स्वनगरमगच्छत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7591)
- **Original**: विजयिने॑ च राजानमशेषपौरभृत्यपरिजनामात्प- समेता झैष्या द्रष्टमथ्चिष्ठानद्वारमागता
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7592)
- **Original**: सा चावल्तेक्य राज्ञ: सव्यपाश्चवरत्तिनीं कन्यामीष- दुद्धृतामर्षस्फुरद्धरपल्लवा राजानमवोचत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7593)
- **Original**: अतिचपलतचित्तात्र स्पयन्दने केय- मारोपितेति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7594)
- **Original**: असावप्यनालोचितोत्तर- बचनो5तिभयात्तामाह स्रुधा ममेयमिति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7595)
- **Original**: अथैन जैव्योवाच
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7596)
- **Original**: नाहं प्रसृता पुत्रेण नान्‍्या पत्यभवत्तव
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7597)
- **Original**: स्लुपासम्बन्धता होषा कतमेन सुतेन ते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7598)
- **Original**: 29 श्षीपराशर उवाच इत्यात्मेष्याकोपकलुषितबत्नमुषितवबिवेको भयादुरुक्तपरिहारार्थमिदमवनीपतिराह
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7599)
- **Original**: बस्ते जनिष्यतः आत्पजस्तस्पेयमनागतस्वैब भार्या निरूपितेत्याकर्ण्योद्धृतमृदुहासा तथेत्याह
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7600)
- **Original**: प्रविवेश च॑ राज्ञा सहाधिष्ठानम्‌
- **Translation**: 

---

