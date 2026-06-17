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

### Verse 1 (Vishnu Puran 0.3101)
- **Original**: ड2 निषध: पारियात्रक्ष मर्यादापर्वतावुभौ । मेरो: पश्चिमदिग्भागे यथा पूर्वे तथा स्थित
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3102)
- **Original**: 43 ब्रिथृज्ञे जारुधिश्षैव उत्तरो वर्षपर्वतो। पूर्वपश्चायतावेतावर्णवान्तर्व्यवस्थितो..._
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3103)
- **Original**: डड इत्येते मुनिवर्योक्ता मर्वादापर्वतास्तव । जठराद्या: स्थिता मेरोस्तेषां द्वौ द्वौ चतुर्दिशम्‌ ।। 45 मेरोश्षतुर्दिझ ये तु प्रोक्ता: केसरपर्वता: । शीतान्ताद्या मुने तेघामतीव हि मनोरमा: । जैलानामन्तरे द्रोण्य:ः सिद्धजारणसेविता:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3104)
- **Original**: 46 सुरम्याणि तथा तासु काननानि पुर णि च। लक्ष्मीविष्ण्वभ्रिसूर्यादिदेवानां मुनिसत्तम । तास्वायतनवर्याणि जुष्टानि वरकिन्नरै:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3105)
- **Original**: 47 गन्धर्ववक्षरक्षांसि तथा दैतेयदानवा: । क्रीडन्ति तासु रम्यासु शैलद्रोणीघ्रहर्निशम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3106)
- **Original**: 48 भौमा होते स्मृता: स्वर्गा धर्मिणामाल्तया मुने । नैतेषु पापकर्माणो यान्ति जन्मशतैरपि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3107)
- **Original**: 49 भद्गाश्चे भगवान्विष्णुरास्ते हयशिरा ट्विज । बराह: केतुमाले तु भारते कूर्मरूपथधुक्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3108)
- **Original**: 50 मत्स्यरूपश्च गोविन्दः कुरुष्वास्ते जनार्दन: । विश्वरूपेण सर्वत्र सर्व: सर्वत्रगों हरि:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3109)
- **Original**: 51 सर्वस्याधारभूतोउसौ मैश्रेयास्तेडखिलात्मक:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3110)
- **Original**: 52 यानि किप्पुरुषादीनि वर्षाण्यष्टी महामुने । नतेषु शोको नायासो नोद्वेगः क्षुद्रधादिकम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3111)
- **Original**: 53 स्वस्थाः प्रजा निरातड्डास्सर्वदुःखबिवर्जिता: । दशद्वादश्वर्षाणां सहस्नाणि स्थिरायुष:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3112)
- **Original**: 54 न तेषु वर्षते देवों भौमान्यप्भांसि तेषु ले । कृतत्रेतादिक॑ नैव तेषुं स्थानेषु कल्पना
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3113)
- **Original**: 55 सर्वेप्वेतेषु वर्षेष्‌ु सप्त सप्त कुछाचला: । नद्यश्व शतहस्तेभ्य: प्रसूता या द्विजोत्तम
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3114)
- **Original**: 56 समान हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3115)
- **Original**: जठर और देवकूट--ये दोनों मर्यादापर्वत है जो उत्तर और दक्षिणकी ओर नील तथा निषधपर्वततक फैले हुए हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3116)
- **Original**: पूर्व और पश्चिमकी ओर फैले हुए गन्धमादन और कैल्लस--ये दो पर्वत जिनका विस्तार अस्सी योजन है, समुद्रके भीतर स्थित हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3117)
- **Original**: पूर्वके समान सेकको पश्चिम ओर भी निषथ और पारियात्र नामक दो मर्यादापर्शत स्थित हैं 43
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3118)
- **Original**: उत्रकी ओर ब्रिशृत़् और जारुधि नामक वर्षपर्तत हैं। ये दोनों पूर्व और पश्चिमकी ओर समुद्रके गर्भमें स्थित हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3119)
- **Original**: इस प्रकार, हे मुनिबर । तुमसे जठर आदि मर्यादापर्वतोंका वर्णन किया, जिनमेंसे दो-दो मेरुकी चारों दिशाओंमें स्थित हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3120)
- **Original**: हे मुने ! मेरुके चारों ओर स्थित जिन दीतान्त आदि केसरपर्वतोके विषयमें तुमसे कहा था, उनके बीचमें सिद्ध-चारणादिसे सेवित अति सुन्दर कन्दराएँ हैं
- **Translation**: 

---

