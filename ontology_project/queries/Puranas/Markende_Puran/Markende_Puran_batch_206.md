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

### Verse 1 (Markende Puran 0.4101)
- **Original**: अज््जा दो है! हाथी, जोड़े, 25 और पैंदलसे युक्त जाग प्रज्वलित हो उठतो है, उसी प्रकार दम
- **Translation**: 

---

### Verse 2 (Markende Puran 0.4102)
- **Original**: जतुरक्षिणी सेना तैयार करो। पिताके चैरका बदला फ्रोक्षग्सिसि जलते हुए #थ-से-हाथ मलने लगे
- **Translation**: 

---

### Verse 3 (Markende Puran 0.4103)
- **Original**: लिये बिना, पित्ताफे हल्यारेक्ता प्राण लिये बिया और इस प्रकार बोल-'ओह ! मुझ पुत्रके जीत्ते-
- **Translation**: 

---

### Verse 4 (Markende Puran 0.4104)
- **Original**: तथा माताजोकी आज्ञाका पालन छिंये ल्िना मुझे जी उस नृशंस्त अपुष्यानने मेरे प्रताकों अनाथकी
- **Translation**: 

---

### Verse 5 (Markende Puran 0.4105)
- **Original**: जोवित रहनेका ठत्साड़ वहीं हैं।' राजाकी यह भाँत्ति मार डाला और इस प्रकार मेरे कुलछा
- **Translation**: 

---

### Verse 6 (Markende Puran 0.4106)
- **Original**: वात सुनकर ख्िन्नचित्त हुए मन्त्रियोंने सेक्‍कों और अमपान किया। यदि मैं बैठकर शोक मनाऊँ वा
- **Translation**: 

---

### Verse 7 (Markende Puran 0.4107)
- **Original**: वाहनोमहित सेझको कूबके लिये तैयार किया क्षमा ऋर दूँ तो यह देरी नपुंझकता है। दुष्टोंका
- **Translation**: 

---

### Verse 8 (Markende Puran 0.4108)
- **Original**: और त्रिकालवेता पुरोहितसे आशोबांद ले सत्र दमग और साधु (क्तोंछा ग्रालन-यहों मेग
- **Translation**: 

---

### Verse 9 (Markende Puran 0.4109)
- **Original**: लोग तलाश, शक्ति और ऋष्ट आदि आयुध लिये कतंव्य हैं। मेंर पिताकों मारा गया देखकर भो
- **Translation**: 

---

### Verse 10 (Markende Puran 0.4110)
- **Original**: नगरसे आहर निकले! महाराज दम नागराजको यादें शत्रु लोवित है तो अब 'हा लात! हा ताव !'
- **Translation**: 

---

### Verse 11 (Markende Puran 0.4111)
- **Original**: भौति कुफ़कारते हुए अपुष्मान्‌कों ओर चले। कहकर बहुत आंधिक विल्गाम कर्नेसे क्‍या होगा।
- **Translation**: 

---

### Verse 12 (Markende Puran 0.4112)
- **Original**: उन्होंने वप्ुम्मान॒के सोमाशक्षक्तों तथा सामन्तोंका इस समय जो करना अवश्यक है, वहीं में
- **Translation**: 

---

### Verse 13 (Markende Puran 0.4113)
- **Original**: चश्च करते हुए, बड़े बेगले दक्षिण दिशामें चढाई करूँगा। उस ऋाथर, पापी एबं दु दक्षिण-
- **Translation**: 

---

### Verse 14 (Markende Puran 0.4114)
- **Original**: की। संकून्दसकुसार अपुष्मानकों यह पता लग देशनिबासी: शत्रुकों युद्धसें #।:+र सप्प्रए पृध्वीका
- **Translation**: 

---

### Verse 15 (Markende Puran 0.4115)
- **Original**: गया क्ति दम दत्ल-बलसहित शा रहा है। इससे राज्य भोगूँगा। यदि उसे न मार सक्रा तो स्वयं ही
- **Translation**: 

---

### Verse 16 (Markende Puran 0.4116)
- **Original**: उसके सनमें त्ततिक भो भय था कम्म नहीं हुआ। आर्नियें प्रवेश कर जाकँगा। गांदे देबराज इन्द्र
- **Translation**: 

---

### Verse 17 (Markende Puran 0.4117)
- **Original**: उसने भी अपनों सेताकों युद्धके लिये तैयार हष्थमें तल लिब्रे स्वर ही एम युद्धमें पघारें,
- **Translation**: 

---

### Verse 18 (Markende Puran 0.4118)
- **Original**: होनेका आदेश दिया और नगरसे बाहर निकलकर भयडूर दष्ड लिये साक्षात््‌ यपराज भो कृषित
- **Translation**: 

---

### Verse 19 (Markende Puran 0.4119)
- **Original**: दफ्के पास दूत 'गेजा। दृतने वहाँ जाकर होकर आ जार्थ, कुजेर, अरुण ओर सूर्य भी
- **Translation**: 

---

### Verse 20 (Markende Puran 0.4120)
- **Original**: ऊहा--'क्त्रिवाथम! तू शीघ्रतापूर्वक मेरे समोप वषुप्सनूओी रक्षाक्ता वत्त करें जो भो में अपने
- **Translation**: 

---

