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

### Verse 1 (Bramha 0.1981)
- **Original**: निमित्त शिला ले आनेके लिये जाओ। अपने साथ पुरुषोत्तमक्षेत्र है, यह बात मुझे मालूम हो गयी;
- **Translation**: 

---

### Verse 2 (Bramha 0.1982)
- **Original**: प्रधान-प्रधान शिल्पियोंको भी, जो शिला खोदनेके क्योंकि यहाँ कल्पवृक्षस्वरूप विशाल बटवृक्ष
- **Translation**: 

---

### Verse 3 (Bramha 0.1983)
- **Original**: काममें निपुण हों, ले लो। विन्ध्याचल बहुत खड़ा है। यहीं इन्द्रनीलमणिकी बनी हुई मणिमयी
- **Translation**: 

---

### Verse 4 (Bramha 0.1984)
- **Original**: विस्तृत पर्वत है। बह अनेकों कन्दराओंसे प्रतिमा है, जिसे भगवानूने स्वयं छिपा दिया है।
- **Translation**: 

---

### Verse 5 (Bramha 0.1985)
- **Original**: सुशोभित है। उसके सभी शिखरोंकों भलीभाँति क्योंकि यहाँ दूसरी कोई प्रतिमा नहीं दिखायी
- **Translation**: 

---

### Verse 6 (Bramha 0.1986)
- **Original**: देखकर सुन्दर-सुन्दर शिलाएँ कटबाओ और देती। मैं ऐसा प्रयत्न करूँगा, जिससे सत्यपराक्रमी
- **Translation**: 

---

### Verse 7 (Bramha 0.1987)
- **Original**: उन्हें छकड़ों तथा नावॉपर लादकर ले आओ, जगदीश्रर भगवान्‌ विष्णु मुझे प्रत्यक्ष दर्शन दें। मैं
- **Translation**: 

---

### Verse 8 (Bramha 0.1988)
- **Original**: विलम्ब न करो।' अनन्य भावसे भगवानूमें मन लगाकर यहाँ यज्ञ, ,. इस प्रकार राजाओंकों शिलाके लिये जानेको दान, तपस्या, होम, ध्यान, पूजन तथा उपवास
- **Translation**: 

---

### Verse 9 (Bramha 0.1989)
- **Original**: आज्ञा दे महाराजने अमात्यों और पुरोहितोंसे आदिके द्वारा विधिपूर्वक उत्तम ब्रतका पालन
- **Translation**: 

---

### Verse 10 (Bramha 0.1990)
- **Original**: कहा-'सर्वत्र शीघ्रगामी दूत भेजे जायेँ और वे करूँगा। साथ ही यहाँ श्रीविष्णु भगवान्‌के मन्दिर पृथ्वीके समस्त राजाओंके पास जाकर मेरी यह
- **Translation**: 

---

### Verse 11 (Bramha 0.1991)
- **Original**: + राजा इन्द्ुप्ठके द्वारा अश्वमेध-यज्ञ तथा पुरुषोत्तम-प्रासाद-निर्माणका कार्य * श्र आज्ञा सुना दें--'राजाओ! महाराज इन्द्रबयाप्नकी , मेरा सब कार्य सम्पन्न हो सकता है।' आज्ञाके अनुसार तुम सब लोग हाथी, घोड़े, रथ
- **Translation**: 

---

### Verse 12 (Bramha 0.1992)
- **Original**: महाराज इन्द्रदुुम्नके यों कहनेपर सब राजाओंको और पैदल सेना तथा अमात्यों एवं पुरोहितोंके
- **Translation**: 

---

### Verse 13 (Bramha 0.1993)
- **Original**: बड़ा हर्ष हुआ। उन्होंने महाराजकी आज्ञासे धन, साथ चलो।' ऐसी आज्ञा पाकर दूत राजाओंके
- **Translation**: 

---

### Verse 14 (Bramha 0.1994)
- **Original**: रत्र, सुवर्ण, मणि, मोती, कम्बल, मृगचर्म, सुन्दर पास गये और सबको महाराजकी आज्ञा सुना दी।
- **Translation**: 

---

### Verse 15 (Bramha 0.1995)
- **Original**: बिछौने, हीरे, पुखराज, माणिक, लाल, नीलम, दक्षिण, पश्चिम, उत्तर और पूर्व देशोंके रहनेवाले,
- **Translation**: 

---

### Verse 16 (Bramha 0.1996)
- **Original**: हाथी, घोड़े, रथ, हथिनी, भाँति-भाँतिके द्रव्य, दूर और समीष निवास करनेवाले, पर्वत तथा
- **Translation**: 

---

### Verse 17 (Bramha 0.1997)
- **Original**: भक्ष्य, भोज्य तथा अनुलेप आदि पदार्थोंकी वर्षा भिन्न-भिन्न ट्वीपोंके निवासी नरेश महारान इन्द्रछुश्लका
- **Translation**: 

---

### Verse 18 (Bramha 0.1998)
- **Original**: की। राजा इन्द्रबुम्नने देखा, यज्ञकी सब सामग्री आदेश सुनकर रथ, हाथी, घोड़े और पैदल
- **Translation**: 

---

### Verse 19 (Bramha 0.1999)
- **Original**: एकत्रित हो गयी है और यज्ञकर्मके ज्ञाता, वेद- सेनाके साथ बहुत धन लेकर भारी संख्यामें
- **Translation**: 

---

### Verse 20 (Bramha 0.2000)
- **Original**: वेदाज्लोंमें पारंगत, शास्त्रज्ञानमें निपुण तथा सब एकत्रित हुए। राजाओंको अमात्यों और पुरोहितोंसहित
- **Translation**: 

---

